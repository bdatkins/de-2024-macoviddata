import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load MA COVID-19 Case Data from the mass.gov website
    """
    url = 'https://www.mass.gov/media/2642851/download'
    case_dtypes = {
       'Confirmed deaths' : pd.Int64Dtype(),
       'Probable deaths' : pd.Int64Dtype(),
       'Confirmed and probable deaths' : pd.Int64Dtype(),
       'Confirmed cases' : pd.Int64Dtype(),
       'Probable cases' : pd.Int64Dtype(),
       'Confirmed and probable cases' : pd.Int64Dtype()
    }

    parse_dates = ['Week Start Date', 'Week End Date', 'Last updated']
    return pd.read_excel(url, 'Weekly Cases and Deaths', dtype=case_dtypes, parse_dates=parse_dates)


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
