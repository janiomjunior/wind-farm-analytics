
{{ config(materialized='table') }}

select
    date(event_timestamp) as event_date,
    avg(lv_activepower_kw) as avg_activepower_kw,
    avg(wind_speed_ms) as avg_wind_speed_ms,
    avg(theoretical_power_curve_kwh) as avg_theoretical_power_curve_kwh,
    avg(wind_direction_deg) as avg_wind_direction_deg,
    count(*) as record_count
from {{ ref('stg_scada') }}
group by event_date
order by event_date