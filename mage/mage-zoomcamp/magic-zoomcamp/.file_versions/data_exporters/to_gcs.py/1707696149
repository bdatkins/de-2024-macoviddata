from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path
import requests
import io
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_google_cloud_storage(**kwargs) -> None:

    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'

    bucket_name = 'warehouse-zoomcamp-barbara-atkins'
    base_object_key = 'green_taxi_2022'
    extension =  ".parquet"
    year = "2022"
    months = ["01","02","03","04","05","06","07","08","09","10","11", "12"]
    base_file_url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_"

 # https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-01.parquet

    for month in months:
        taxi_data_url_by_month = base_file_url + year + "-" + month + extension
        object_key = base_object_key + "_" + month + extension
        response = requests.get(taxi_data_url_by_month)
        data = io.BytesIO(response.content)
        df = pq.read_table(data).to_pandas()

        df['VendorID'] = pd.to_numeric(df['VendorID'])
        df['passenger_count']       = pd.to_numeric(df['passenger_count'])
        df['trip_distance']         = pd.to_numeric(df['trip_distance'])
        df['RatecodeID']            = pd.to_numeric(df['RatecodeID'])
        df['store_and_fwd_flag']    = df['store_and_fwd_flag'].astype(str)
        df['PULocationID']          = pd.to_numeric(df['PULocationID'])
        df['DOLocationID']          = pd.to_numeric(df['DOLocationID'])
        df['payment_type']          = pd.to_numeric(df['payment_type'])
        df['fare_amount']           = pd.to_numeric(df['fare_amount'])
        df['extra']                 = pd.to_numeric(df['extra'])
        df['mta_tax']               = pd.to_numeric(df['mta_tax'])
        df['tip_amount']            = pd.to_numeric(df['tip_amount'])
        df['tolls_amount']          = pd.to_numeric(df['tolls_amount'])
        df['improvement_surcharge'] = pd.to_numeric(df['improvement_surcharge'])
        df['total_amount']          = pd.to_numeric(df['total_amount'])
        df['congestion_surcharge']  = pd.to_numeric(df['congestion_surcharge'])
        df["ehail_fee"]             = pd.to_numeric(df["ehail_fee"])
      #  df["lpep_pickup_datetime"]  = df["lpep_pickup_datetime"].astype(str)
      #  df["lpep_dropoff_datetime"]  = df["lpep_dropoff_datetime"].astype(str)


        GoogleCloudStorage.with_config(
            ConfigFileLoader(
                config_path,
                config_profile
                )
            ).export(
                df,
                bucket_name,
                object_key
            )
