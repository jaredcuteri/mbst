import AbstractIMU
import Adafruit_ADXL345
from DocInherit import doc_inherit

class Adxl345(AbstractIMU.AbstractIMU):

    def __init__(self):
        self.imu = Adafruit_ADXL345.ADXL345()
        super().__init__()
    
    @doc_inherit
    def setRange(self, exactRange):
        selRange = exactRange 
        # TODO: add range ceil functionality to 2, 4, 8, 16
        self.imu.set_range(selRange)

    @doc_inherit
    def getRange(self):
        return self.imu.get_range()

    @doc_inherit
    def setDataRate(self, exactDataRate):
        selDataRate = exactDataRate
        # TODO: Add ceil functionality
        self.imu.set_data_rate(selDataRate)
    
    @doc_inherit
    def getDataRate(self):
        return self.imu.get_data_rate()

    @doc_inherit 
    def getAccels(self):
        # TODO: Incorporate Adafruit_ADXL345 docstring
        return self.imu.read() 

    @doc_inherit
    def getRates(self):
        '''
        No Gyro's Present on ADXL345
        '''
        return (None, None, None)

