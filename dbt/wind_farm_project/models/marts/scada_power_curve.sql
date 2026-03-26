{{ config(materialized='table') }}

select
    round(wind_speed_ms, 1) as wind_speed_bucket,
    avg(lv_activepower_kw) as avg_power,
    avg(theoretical_power_curve_kwh) as avg_theoretical_power,
    count(*) as record_count
from {{ ref('stg_scada') }}
group by wind_speed_bucket
order by wind_speed_bucket