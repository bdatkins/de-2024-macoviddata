{{
    config(
        materialized='table'
    )
}}

select * from {{ ref('stg_staging__case_data') }}
