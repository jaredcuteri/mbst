import csv
import datetime

class Logger():
    
    startTime = datetime.datetime.now() 
    startTimeAbrv = startTime.strftime("_%Y%m%d_%H%M%S")
    startTimeStr = startTime.strftime("%Y-%m-%d %H:%M:%S")
    
    def __init__(self, filename="DataLog",desc="Data Log"):
        self.logFile = open(filename+startTimeAbrv+".csv","w")
        self.logWriter = csv.writer(self.logFile, delimiter=',')
        self.logFile.write(desc + "\n")
        self.logFile.write("Recording Started at: " + Logger.startTimeStr)
    
    def writeString(self,string):
        self.logFile.write(string)
            
    def writeHeader(self, header):
        self.logWriter.writerow(header)
        
    def writeData(self, data):
        self.logWriter.writerow(data)