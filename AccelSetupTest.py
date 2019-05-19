import board
import busio
from collections import OrderedDict
from datetime import datetime
from ImuPalace import Adxl345
from ImuPalace import Mma8451
import Logger
import time

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

mpss2g = 1/9.81
dataPrecision = 6 
# Necessary to ensure data is output in correct order
sensors = OrderedDict()
# Instantiate sensors
sensors['MMA8451'] = Mma8451.Mma8451()
sensors['ADXL345'] = Adxl345.Adxl345()
dataRate = 400 #Hz
# Configure sensor settings
for sensor in sensors.values():
    sensor.setRange(8)
    sensor.setDataRate(dataRate)

# Save off data collection start time
startTime = datetime.now()

# Log File Setup
dataLog = Logger.Logger(filename="AccelData")
AccelConfigStr = ""
DataHeaderStr = "t[s] "
for idx, name in enumerate(sensors.keys()):
    AccelConfigStr += "Accel#"+str(idx)+" "+name+" "
    DataHeaderStr += "Ax"+str(idx)+"[g] Ay"+str(idx)+"[g] Az"+str(idx)+"[g] "
dataLog.writeString(AccelConfigStr+"\n")
dataLog.writeHeader(DataHeaderStr.split(" "))
dataSamples = 0
while True:
    currTime = datetime.now()
    relTime = currTime-startTime
    dataOut = [relTime.total_seconds(),]
    for name, sensor in sensors.items():
        dataOut += sensor.getAccels()    
    dataOut = [ round(datum,dataPrecision) for datum in dataOut ]
    dataLog.writeData(dataOut)
    dataSamples += 1
    print( "Data Samples Collected: "+str(dataSamples), end='\r')
    # Save Accels to file
    # Getting about 40 Hz with sleep
    #time.sleep(1/dataRate)
