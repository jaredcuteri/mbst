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
numSamp = 40
sensors = {}
accelHist = {}
timeHist = [0] * numSamp
time.sleep(0.2) # Sleep necessary to avoid I/O error (Why?)
sensors['mma'] = Mma8451.Mma8451()
accelHist['mma'] = [(0, 0, 0), ] * numSamp
time.sleep(0.2)
sensors['adxl'] = Adxl345.Adxl345()
accelHist['adxl'] = [(0, 0, 0), ] * numSamp

# Configure sensor settings
for sensor in sensors.values():
    sensor.setRange(8)
    sensor.setDataRate(800)

# Set up plot
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
style.use('fivethirtyeight')

# Save off data collection start time
start_time = datetime.now()

ln, = plt.plot([], [], 'ro')

def init():
    return ln,    
def animate(i):
    # TODO: instead of pop/append use queue
    samp_time = datetime.now()
    delt_time = samp_time - start_time
    time_s = delt_time.seconds + (delt_time.microseconds)*1e-6
    timeHist.pop()
    timeHist.append(time_s)

    for name, sensor in sensors.items():
        _ = accelHist[name].pop()
        accelHist[name].append(sensor.getAccels())
    
    ax1.clear()
    ln.set_data(timeHist,list([accels[2] for accels in accelHist['adxl']]))
    return ln,
ani = animation.FuncAnimation(fig, animate,init_func=init, blit=True, interval=500)
Writer = animation.writers['html']
writer = Writer(fps=2, metadata=dict(artist='Me'), bitrate=1800)
ani.save('test.html',writer=writer)

while True:
    time.sleep(0.5)
