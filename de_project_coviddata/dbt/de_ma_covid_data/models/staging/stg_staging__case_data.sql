with 

source as (

    select * from {{ source('staging', 'case_data') }}

),

renamed as (

    select
        id,
        week_start_date,
        week_end_date,
        confirmed_deaths,
        probable_deaths,
        confirmed_and_probable_deaths,
        confirmed_cases,
        probable_cases,
        confirmed_and_probable_cases,
        last_updated

    from source

)

select * from renamed
