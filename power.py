# Pool Pump Energy and Cost Estimator
# Assumes power ∝ RPM^3

def estimate_energy_and_cost(schedule, base_rpm=3450, base_power_watts=2130, electricity_rate=0.15):
    """
    schedule: list of tuples (rpm, hours)
    base_rpm: RPM at which base_power_watts is measured
    base_power_watts: actual power draw at base_rpm
    electricity_rate: cost per kWh in USD
    """
    total_energy_kwh = 0
    print("RPM\tHours\tPower (W)\tEnergy (kWh)")
    for rpm, hours in schedule:
        relative_power = (rpm / base_rpm) ** 3
        actual_power = base_power_watts * relative_power
        energy_kwh = (actual_power * hours) / 1000
        total_energy_kwh += energy_kwh
        print(f"{rpm}\t{hours}\t{actual_power:.1f}\t\t{energy_kwh:.2f}")
    
    total_cost = total_energy_kwh * electricity_rate
    print(f"\nTotal Energy: {total_energy_kwh:.2f} kWh")
    print(f"Estimated Daily Cost: ${total_cost:.2f}")

# Example usage
#schedule = [ (3450, 6),  (2450, 6),  (2000, 12) ]
schedule = [ (3000, 6),  (1000, 6),  (2450, 6), (1000, 6) ]

estimate_energy_and_cost(schedule, base_rpm=3450, base_power_watts=2130, electricity_rate=0.15)

