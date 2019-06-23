import csv
import datetime
import os
import os.path as path

class Logger():
    
    def __init__(self, filename="DataLog",filepath=".", desc="Data Log"):
        startTime = datetime.datetime.now() 
        startTimeAbrv = startTime.strftime("_%Y%m%d_%H%M%S")
        startTimeStr = startTime.strftime("%Y-%m-%d %H:%M:%S")
        self.filename = path.join(filepath, filename+startTimeAbrv+".csv")
        if not path.isdir(filepath):
            os.mkdir(filepath)
        self.logFile = open(self.filename,"w")
        self.logWriter = csv.writer(self.logFile, delimiter=',')
        self.logFile.write(desc + "\n")
        self.logFile.write("Recording Started at: " + startTimeStr+"\n")
    
    def writeString(self,string):
        self.logFile.write(string)
            
    def writeHeader(self, header):
        self.logWriter.writerow(header)
        
    def writeData(self, data):
        self.logWriter.writerow(data)

    def close(self):
        self.logFile.close()
