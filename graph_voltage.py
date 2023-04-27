import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

FILENAME = "voltage.txt"

# Read data from text file
with open(FILENAME, 'r') as fp:
    data = fp.readlines()

# Convert data to numpy array
data = np.array([list(map(float, x.strip().split())) for x in data])

# Extract time and voltage data
time = data[:, 0]
voltage = data[:, 1]

# Apply moving mean filter
window = 2500
voltage2 = pd.Series(voltage).rolling(window).mean()

# Plot data
plt.plot(time, voltage2, "-b")
plt.xlabel('Time (s)')
plt.ylabel('Voltage (mV)')
plt.show()
