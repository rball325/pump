def estimate(
    schedule,
    base_rpm=3450,
    base_power_watts=2130,
    base_flow_gpm=None,
    electricity_rate=0.15,
    pool_volume_gallons=None
):
    show_flow = base_flow_gpm is not None

    header = "RPM\tHours\tPower (W)\tEnergy (kWh)"
    if show_flow:
        header += "\tFlow (GPM)\tGallons Moved"
    print(header)

    total_energy_kwh = 0
    total_gallons_moved = 0

    for rpm, hours in schedule:
        power = base_power_watts * (rpm / base_rpm) ** 3
        energy_kwh = (power * hours) / 1000
        total_energy_kwh += energy_kwh

        row = f"{rpm}\t{hours}\t{power:.1f}\t\t{energy_kwh:.2f}"
        if show_flow:
            flow_gpm = base_flow_gpm * (rpm / base_rpm)
            gallons = flow_gpm * 60 * hours
            total_gallons_moved += gallons
            row += f"\t\t{flow_gpm:.1f}\t\t{gallons:.0f}"
        print(row)

    total_cost = total_energy_kwh * electricity_rate
    print(f"\nTotal Energy: {total_energy_kwh:.2f} kWh")
    print(f"Estimated Cost: ${total_cost:.2f}")

    if show_flow and pool_volume_gallons:
        print(f"Total Gallons Moved: {total_gallons_moved:.0f}")
        print(f"Estimated Turnovers: {total_gallons_moved / pool_volume_gallons:.2f} per day")
