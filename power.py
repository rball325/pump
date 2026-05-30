from pump import estimate

schedule = [(3000, 6), (1000, 6), (2450, 6), (1000, 6)]

estimate(schedule, electricity_rate=0.15)
