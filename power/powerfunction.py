import numpy as np
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = "Sample-2.csv"
dt = 0.2

samples, power = np.genfromtxt(file_path, delimiter=",", skip_header=14, usecols=(0, 3), unpack=True)

mask = ~np.isnan(power)
samples = samples[mask]
power = power[mask]

power_mW = power * 1000
time = samples * dt

steady = power_mW[-50:].mean()
on_idx = np.argmax(power_mW > 0.5 * steady)
t_on = time[on_idx]

band = 0.02 * steady
within = np.abs(power_mW - steady) <= band
t_settle = None
for i in range(len(within)):
    if within[i] and within[i:].mean() > 0.95:
        t_settle = time[i]
        break
settling_time = t_settle - t_on

print("Steady power =", round(steady, 3), "mW")
print("Turn-on time =", round(t_on, 1), "s")
print("Settled at =", round(t_settle, 1), "s")
print("Settling time =", round(settling_time, 1), "s")

plt.figure(figsize=(10, 5))
plt.plot(time, power_mW, linewidth=1.5, label="Measured power")
plt.axhline(steady, linestyle="--", color="green", label="Steady = " + str(round(steady, 3)) + " mW")
plt.axvline(t_settle, linestyle="--", color="red", label="Settled at " + str(round(t_settle, 1)) + " s")
plt.xlabel("Time (s)")
plt.ylabel("Power (mW)")
plt.title("Laser Power Output vs Time")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
