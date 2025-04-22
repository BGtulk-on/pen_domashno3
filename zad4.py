import random

def temperature_monitor():
    for _ in range(4):
        temp = round(random.uniform(2.0, 8.0), 2)
        yield temp

for temp in temperature_monitor():
    print(f"Температура: {temp}°C")