from .AbstractIMU import AbstractIMU
import adafruit_mma8451 as mma
import board
import busio


class Mma8451(AbstractIMU):

    def __init__(self):
        self.imu = mma.MMA8451(busio.I2C(board.SCL, board.SDA))
        super().__init__()
    
    def setRange(self, exactRange):
        RangeMap = {
                2 : mma.RANGE_2G,
                4 : mma.RANGE_4G,
                8 : mma.RANGE_8G
                }
        selRange = exactRange 
        # TODO: add range ceil functionality to 2, 4, 8, 16
        self.imu.range = RangeMap[selRange]
            
    def getRange(self):
        return self.imu.range

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
    
    def getDataRate(self):
        return self.imu.data_rate

    def getAccels(self):
        # TODO: Calibrate
        mpss2g = 1/9.81
        raw_accels = self.imu.acceleration
        accelsG = tuple([mpss2g*acc for acc in raw_accels])
        return accelsG

    def getRates(self):
        '''
        No Gyro's Present on MMA8451
        '''
        return (None, None, None)

