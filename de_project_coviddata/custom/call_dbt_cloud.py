from mage_ai.services.dbt.dbt import DbtCloudClient

@custom
def transform_custom(*args, **kwargs):
    """
    Trigger dbt cloud model run to further transform data
    """
    dbt_account_id = 244343
    dbt_api_token = 'dbtc_zwrNCKoDiqd7fVOr-Sf5eXK3O9TCAyfY8kTMDnMuRGWtgB_jvQ'
    dbt_job_id = 563528
    client = DbtCloudClient(dict(account_id=dbt_account_id, api_token=dbt_api_token))
    client.trigger_job_run(dbt_job_id, poll_status=True)
    return {}

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
