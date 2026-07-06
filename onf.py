from pump import estimate

schedule = [
    (2750, 6), # High speed
    (1650, 6), # Low speed
    (2450, 6), # Medium speed
    (1650, 6), # Low speed
]

estimate(
    schedule,
    base_rpm=3450,
    base_power_watts=2130,
    base_flow_gpm=150,
    electricity_rate=0.15,
    pool_volume_gallons=33000
)
