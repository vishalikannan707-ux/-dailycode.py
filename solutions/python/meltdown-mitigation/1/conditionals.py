def is_criticality_balanced(temperature, neutrons_emitted):
    return (temperature < 800 and
            neutrons_emitted > 500 and
            temperature * neutrons_emitted < 500000)

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    criticality = temperature * neutrons_produced_per_second
    lower_bound = 0.9 * threshold
    upper_bound = 1.1 * threshold

    if criticality < lower_bound:
        return 'LOW'
    elif lower_bound <= criticality <= upper_bound:
        return 'NORMAL'
    else:
        return 'DANGER'
# Test 1
print(is_criticality_balanced(750, 600))  # True

# Test 2
print(reactor_efficiency(200, 50, 15000))  # 'orange'

# Test 3
print(fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000))  # 'DANGER'
