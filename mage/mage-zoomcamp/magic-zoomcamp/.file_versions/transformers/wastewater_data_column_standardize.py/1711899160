if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(data, *args, **kwargs):
    """
    Standardize columnn names for wastewater data
    """
    data.columns = (data.columns
                       .str.replace('(', '')
                       .str.replace(')', '')
                       .str.replace(' ', '_')
                       .str.replace('-', '_')
                       .str.lower())

    data.rename(columns = {
       "7_day_average_of_sars_cov_2_concentration": "weekly_average_sars_cov_2"}, inplace=True)
       
    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
