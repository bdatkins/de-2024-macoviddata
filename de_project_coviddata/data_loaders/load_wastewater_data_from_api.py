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
    Load MA COVID-19 Wastewater Data from the mass.gov website
    """
    url = 'https://www.mass.gov/media/2642316/download'
    wastewater_dtypes = {
       'Tester' : str,
       'Site type' : str,
       'Name of Sampling Location' : str,
       '7 day average of SARS-CoV-2 concentration' : float,
       'Number of samples in the last 7 days' : pd.Int64Dtype(),
       'SARS-CoV-2 Detected' : str,
       'Units (measuring concentration)' : str,
       'City of sampling location' : str,
       'State of sampling location' : str,
       'County of sampling location' : str
    }
    
    parse_dates = ['Date data last updated', 'Sample collection date']
    return pd.read_excel(url, 'Wastewater Testing Data', dtype=wastewater_dtypes, parse_dates = parse_dates, index_col=0)

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
