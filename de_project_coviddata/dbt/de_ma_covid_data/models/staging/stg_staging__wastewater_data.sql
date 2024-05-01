with 

source as (

    select * from {{ source('staging', 'wastewater_data') }}

),

renamed as (

    select
        tester,
        site_type,
        name_of_sampling_location,
        weekly_average_sars_cov_2,
        number_of_samples_in_the_last_7_days,
        sars_cov_2_detected,
        sample_collection_date,
        units_measuring_concentration,
        city_of_sampling_location,
        state_of_sampling_location,
        county_of_sampling_location,
        date_data_last_updated

    from source

    where state_of_sampling_location='MA'
    
)

select * from renamed