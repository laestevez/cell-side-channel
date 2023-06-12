import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FILENAME = "voltage.txt"

# Read data from text file
with open(FILENAME, 'r') as fp:
    data = fp.readlines()[1:]

# Convert data to numpy array
data = np.array([list(map(float, x.strip().split())) for x in data])

# Extract time and voltage data
time = data[:, 0]
voltage = data[:, 1]

# Apply moving mean filter, window size should be changed for different results.
window_size = 2500
voltage_filtered = pd.Series(voltage).rolling(window_size).mean()

# Plot data
#plt.plot(time, voltage, "-b")
plt.plot(time, voltage_filtered, "-r")
plt.xlabel('Time')
plt.ylabel('Voltage (mV)')
plt.legend()
plt.show()
