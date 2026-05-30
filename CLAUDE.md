# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the scripts

```bash
python3 power.py
python3 onf.py
python3 pnf.py
```

No dependencies beyond the Python standard library. No build step, no virtual environment required.

## Architecture

`pump.py` is the shared library. All three scripts import `estimate()` from it and are otherwise just a schedule + one function call.

```
pump.py        # shared estimate() function
power.py       # energy/cost only (no flow)
onf.py         # energy + flow + turnovers
pnf.py         # same as onf.py, different schedule
```

### estimate() signature

```python
estimate(schedule, base_rpm, base_power_watts, base_flow_gpm, electricity_rate, pool_volume_gallons)
```

- `schedule` — list of `(rpm, hours)` tuples summing to 24 hrs
- `base_flow_gpm` — optional; omit to suppress flow/turnover output (as in `power.py`)
- `pool_volume_gallons` — optional; omit to suppress turnover calculation

### Physics

- **Power ∝ RPM³** — half speed = ~1/8 the power
- **Flow ∝ RPM** — half speed = half the flow rate

To derive RPM from a target flow rate: `rpm = base_rpm × (target_gpm / base_flow_gpm)`

### Pump parameters in use

- `base_rpm = 3450`, `base_power_watts = 2130`, `base_flow_gpm = 150`
- `pool_volume_gallons = 33000`
- `electricity_rate = 0.15` $/kWh
