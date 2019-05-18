import board
import busio
from ImuPalace import Adxl345
from ImuPalace import Mma8451
import time

mpss2g = 1/9.81

# TODO: Make Homogenous wrapper class that creates common interface for MMA and ADXL
sensors = {}
time.sleep(0.2) # Sleep necessary to avoid I/O error (Why?)
sensors['mma'] = Mma8451.Mma8451()
time.sleep(0.2)
sensors['adxl'] = Adxl345.Adxl345()

for sensor in sensors.values():
    sensor.setRange(8)
    sensor.setDataRate(800)


while True:
   # xg_adxl, yg_adxl, zg_adxl = tuple([mpss2g*acc for acc in (x_adxl, y_adxl, z_adxl)])i
    for name, sensor in sensors.items():
        xg, yg, zg = sensor.getAccels()
        print('{0}  Ax={1:6.3f} Ay={2:6.3f} Az={3:6.3f}'.format(name, xg, yg, zg))    
    time.sleep(0.5)
