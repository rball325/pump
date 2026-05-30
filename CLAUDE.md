# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Running the scripts

```bash
python power.py
python onf.py
python pnf.py
```

No dependencies beyond the Python standard library. No build step, no tests, no virtual environment required.

## What this project does

Three standalone Python scripts that estimate pool pump energy consumption and operating cost, using the centrifugal pump affinity laws:

- **Power scales as RPM³** — a pump running at half speed uses ~1/8 the power
- **Flow scales linearly with RPM** — half speed yields half the flow rate

Each script takes a `schedule` (list of `(rpm, hours)` tuples) and pump parameters, then prints a per-segment breakdown plus daily totals.

| Script | Outputs |
|--------|---------|
| `power.py` | Power (W), energy (kWh), daily cost |
| `onf.py` | Same + flow (GPM), gallons moved, pool turnovers |
| `pnf.py` | Same as `onf.py` with a different test schedule |

`onf.py` and `pnf.py` share the same `estimate_energy_flow_cost` function — they differ only in the example `schedule` at the bottom. `onf.py` tests higher RPM speeds; `pnf.py` tests a lower-RPM, lower-energy schedule.

## Key parameters

All functions accept these keyword arguments (with sensible defaults):

- `base_rpm` / `base_power_watts` / `base_flow_gpm` — measured values from the pump spec sheet at a known operating point
- `electricity_rate` — $/kWh (default 0.13–0.15 depending on script)
- `pool_volume_gallons` — used to calculate daily turnovers

To model a different pump or pool, change these values at the call site in the script's `__main__` block.
