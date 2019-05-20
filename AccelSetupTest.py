import board
import busio
from collections import OrderedDict
from datetime import datetime
from ImuPalace import Adxl345
from ImuPalace import Mma8451
import Logger
import RPi.GPIO as GPIO
import time

mpss2g = 1/9.81
dataPrecision = 6 

# GPIO Pin Setup
runningPin = 21
recordPin = 20
recSwitchPin = 16
GPIO.setup(runningPin, GPIO.OUT) # Code Running LED
GPIO.setup(recordPin, GPIO.OUT) # Data Recording LED
GPIO.setup(recSwitchPin, GPIO.IN)

codeRunning = True
dataRecording = False
GPIO.output(runningPin, codeRunning)
GPIO.output(recordPin, dataRecording)

# Necessary to ensure data is output in correct order
sensors = OrderedDict()
# Instantiate sensors
sensors['MMA8451'] = Mma8451.Mma8451()
sensors['ADXL345'] = Adxl345.Adxl345()
dataRate = 200 #Hz
# Configure sensor settings
for sensor in sensors.values():
    sensor.setRange(8)
    sensor.setDataRate(dataRate)


# Log File Setup
AccelConfigStr = ""
DataHeaderStr = "t[s] "
for idx, name in enumerate(sensors.keys()):
    AccelConfigStr += "Accel#"+str(idx)+" "+name+" "
    DataHeaderStr += "Ax"+str(idx)+"[g] Ay"+str(idx)+"[g] Az"+str(idx)+"[g] "
firstPassRec = True
firstPassOff = True
recordData = False
# Add power switch
while True:
    if recordData:
        if firstPassRec:
            firstPassOff = True
            dataRecording = True
            GPIO.output(recordPin, dataRecording)
            dataLog = Logger.Logger(filename="AccelData",filepath="../mbst_data/")
            dataLog.writeString(AccelConfigStr+"\n")
            dataLog.writeHeader(DataHeaderStr.split(" "))
            print('',end='\n')
            print('Writing Output to: ' + dataLog.filename)
            # Save off data collection start time
            startTime = datetime.now()
            dataSamples = 0
            firstPassRec = False
            
        currTime = datetime.now()
        relTime = currTime-startTime
        dataOut = [relTime.total_seconds(),]
        for name, sensor in sensors.items():
            dataOut += sensor.getAccels()    
        dataOut = [ round(datum,dataPrecision) for datum in dataOut ]
        dataLog.writeData(dataOut)
        dataSamples += 1
        print( "Data Samples Collected: "+str(dataSamples), end='\r')
    else:
        # Check Switch
        if firstPassOff:
            firstPassRec = True
            dataRecording = False
            GPIO.output(recordPin, dataRecording)
            firstPassOff = False
        
    if GPIO.input(recSwitchPin):
        recordData = not recordData
        time.sleep(1)

codeRunning = False
GPIO.output(runningPin, codeRunning)
