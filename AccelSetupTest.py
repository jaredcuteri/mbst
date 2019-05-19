import board
import busio
from ImuPalace import Adxl345
from ImuPalace import Mma8451
from datetime import datetime
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

mpss2g = 1/9.81

# Instantiate sensors
time.sleep(0.2) # Sleep necessary to avoid I/O error (Why?)
sensors['mma'] = Mma8451.Mma8451()
time.sleep(0.2)
sensors['adxl'] = Adxl345.Adxl345()
dataRate = 800 #Hz
# Configure sensor settings
for sensor in sensors.values():
    sensor.setRange(8)
    sensor.setDataRate(dataRate)

# Save off data collection start time
start_time = datetime.now()
while True:
    for name, sensor in sensors.items():
        accelerations[name].append(sensor.getAccels())
    # Save Accels to file
    time.sleep(1/dataRate)
