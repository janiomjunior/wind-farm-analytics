select
    parse_timestamp('%d %m %Y %H:%M', date_time) as event_timestamp,
    cast(lv_activepower_kw as float64) as lv_activepower_kw,
    cast(wind_speed_ms as float64) as wind_speed_ms,
    cast(theoretical_power_curve_kwh as float64) as theoretical_power_curve_kwh,
    cast(wind_direction_deg as float64) as wind_direction_deg
from `wind-farm-analytics-janio.wind_farm.scada_raw`