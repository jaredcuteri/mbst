import board
import busio
import adafruit_mma8451 as imu_mma
import Adafruit_ADXL345 as imu_adxl
import time

mpss2g = 1/9.81

i2c = busio.I2C(board.SCL, board.SDA)

# TODO: Make Homogenous wrapper class that creates common interface for MMA and ADXL

# MMA8451 Set Up
time.sleep(0.2)
sensor_mma = imu_mma.MMA8451(i2c)
sensor_mma.range     = imu_mma.RANGE_8G # 2G, 4G, 8G
sensor_mma.data_rate = imu_mma.DATARATE_800HZ # 800, 400, 200, 100, 50, 12.5, 6.25, 1.56

# ADXL345 Set up
time.sleep(0.2)
sensor_adxl = imu_adxl.ADXL345()
sensor_adxl.set_range(imu_adxl.ADXL345_RANGE_2_G)
sensor_adxl.set_data_rate(imu_adxl.ADXL345_DATARATE_800_HZ)

while True:
    x_mma, y_mma, z_mma = sensor_mma.acceleration
    xg_mma, yg_mma, zg_mma = tuple([mpss2g*acc for acc in (x_mma, y_mma, z_mma)])
    xg_adxl, yg_adxl, zg_adxl = sensor_adxl.read()
   # xg_adxl, yg_adxl, zg_adxl = tuple([mpss2g*acc for acc in (x_adxl, y_adxl, z_adxl)])
    print('MMA  Ax={0:6.3f} Ay={1:6.3f} Az={2:6.3f}'.format(xg_mma, yg_mma, zg_mma))    
    print('ADXL Ax={0:6.3f} Ay={1:6.3f} Az={2:6.3f}'.format(xg_adxl, yg_adxl, zg_adxl))    
    time.sleep(0.5)
