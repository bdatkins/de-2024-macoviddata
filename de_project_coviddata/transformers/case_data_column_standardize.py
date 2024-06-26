if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Standardize columnn names for case data
    """
    data.columns = (data.columns
                       .str.replace(' ', '_')
                       .str.lower())
    data.rename(columns = {
       "unnamed:_0": "id"}, inplace=True)

    return data

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
