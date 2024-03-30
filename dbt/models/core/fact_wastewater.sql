{{
    config(
        materialized='table'
    )
}}

select * from {{ ref('stg_staging__wastewater_data') }}
