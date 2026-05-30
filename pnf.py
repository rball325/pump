def estimate_energy_flow_cost(
    schedule,
    base_rpm=3450,
    base_power_watts=1000,
    base_flow_gpm=90,
    electricity_rate=0.13,
    pool_volume_gallons=20000
):
    """
    schedule: list of tuples (rpm, hours)
    base_rpm: RPM at which base_power_watts and base_flow_gpm are measured
    base_power_watts: actual power draw at base_rpm
    base_flow_gpm: flow rate at base_rpm
    electricity_rate: cost per kWh in USD
    pool_volume_gallons: total pool volume
    """
    total_energy_kwh = 0
    total_gallons_moved = 0

    print("RPM\tHours\tPower (W)\tEnergy (kWh)\tFlow (GPM)\tGallons Moved")
    for rpm, hours in schedule:
        relative_power = (rpm / base_rpm) ** 3
        actual_power = base_power_watts * relative_power
        energy_kwh = (actual_power * hours) / 1000

        flow_gpm = base_flow_gpm * (rpm / base_rpm)
        gallons_moved = flow_gpm * 60 * hours

        total_energy_kwh += energy_kwh
        total_gallons_moved += gallons_moved

        print(f"{rpm}\t{hours}\t{actual_power:.1f}\t\t{energy_kwh:.2f}\t\t{flow_gpm:.1f}\t\t{gallons_moved:.0f}")

    total_cost = total_energy_kwh * electricity_rate
    turnovers = total_gallons_moved / pool_volume_gallons

    print(f"\nTotal Energy: {total_energy_kwh:.2f} kWh")
    print(f"Estimated Cost: ${total_cost:.2f}")
    print(f"Total Gallons Moved: {total_gallons_moved:.0f}")
    print(f"Estimated Turnovers: {turnovers:.2f} per day")

# Example usage
schedule = [
    (2750, 6), # High speed
    (1500, 6), # Low speed
    (2450, 6), # Medium speed
    (1500, 6)  # Low speed
]

estimate_energy_flow_cost(
    schedule,
    base_rpm=3450,
    base_power_watts=2130,
    base_flow_gpm=150,
    electricity_rate=0.15,
    pool_volume_gallons=33000
)

