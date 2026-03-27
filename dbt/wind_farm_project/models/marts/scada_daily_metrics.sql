{{ config(
    materialized='table',
    partition_by={
        "field": "event_date",
        "data_type": "date"
    }
) }}

SELECT
    DATE(event_timestamp) AS event_date,
    AVG(lv_activepower_kw) AS avg_activepower_kw,
    AVG(wind_speed_ms) AS avg_wind_speed_ms,
    AVG(theoretical_power_curve_kwh) AS avg_theoretical_power_curve_kwh,
    AVG(wind_direction_deg) AS avg_wind_direction_deg,
    COUNT(*) AS record_count
FROM {{ ref('stg_scada') }}
GROUP BY event_date