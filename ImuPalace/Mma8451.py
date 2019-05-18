import AbstractIMU
import adafruit_mma8451 as mma
import board
import busio:

from DocInherit import doc_inherit

class Mma8451(AbstractIMU.AbstractIMU):

    def __init__(self):
        self.imu = mma()
        super().__init__()
    
    @doc_inherit
    def setRange(self, exactRange):
        RangeMap = {
                2 : mma.RANGE_2G,
                4 : mma.RANGE_4G,
                8 : mma.RANGE_8G
                }
        selRange = exactRange 
        # TODO: add range ceil functionality to 2, 4, 8, 16
        self.imu.range = RangeMap[selRange]
            
    @doc_inherit
    def getRange(self):
        return self.imu.range

    @doc_inherit
    def setDataRate(self, exactDataRate):
        DataRateMap = {
                1  : mma.DATARATE_1_56HZ,
                6  : mma.DATARATE_6_25HZ,
                12 : mma.DATARATE_12_5HZ,
                50 : mma.DATARATE_50HZ,
                100: mma.DATARATE_100HZ,
                200: mma.DATARATE_200HZ,
                400: mma.DATARATE_400HZ,
                800: mma.DATARATE_800HZ
                }
        selDataRate = exactDataRate
        # TODO: Add ceil functionality
        self.imu.data_rate = DataRateMap[selDataRate]
    
    @doc_inherit
    def getDataRate(self):
        return self.imu.data_rate

    @doc_inherit 
    def getAccels(self):
        # TODO: Calibrate
        mpss2g = 1/9.81
        raw_accels = self.imu.acceleration
        accelsG = tuple([mpss2g*acc for acc in raw_accels])
        return accelsG

    @doc_inherit
    def getRates(self):
        '''
        No Gyro's Present on MMA8451
        '''
        return (None, None, None)

