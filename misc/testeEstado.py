import random

# Optional: make runs reproducible
random.seed(42)

states = [0, 0, 0, 0]

def state1(n, states):
    states[0] += 1
    print(f"arrived at state one n = {n:.3f}")
    n += random.uniform(-0.05, 0.07)  # small random step
    return n

def state2(n, states):
    states[1] += 1
    print(f"arrived at state two n = {n:.3f}")
    n += random.uniform(-1, 1)  # moderate step
    return n

def state3(n, states):
    states[2] += 1
    print(f"arrived at state three n = {n:.3f}")
    n += random.uniform(-0.2, 0.4)  # slightly bigger step
    return n

def state4(n, states):
    states[3] += 1
    print(f"arrived at state four n = {n:.3f}")
    n += random.uniform(-61, 30)  # slightly bigger step
    return n

# initial value
n = 1

while True:
    if 0 < n < 10:
        n = state1(n, states)
    elif 10 <= n < 30:
        n = state2(n, states)
    elif 30 <= n < 60:
        n = state3(n, states)
    elif 60 <= n < 200:
        n = state4(n, states)
    else:
        print(f"out of state n = {n:.3f}")
        break

# statistics
print("\nstats:")
print(f"state 1: {states[0]} times")
print(f"state 2: {states[1]} times")
print(f"state 3: {states[2]} times")
print(f"state 4: {states[3]} times")
