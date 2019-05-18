from .AbstractIMU import AbstractIMU
import Adafruit_ADXL345 as adxl

class Adxl345(AbstractIMU):

    def __init__(self):
        self.imu = adxl.ADXL345()
        super().__init__()
    
    def setRange(self, exactRange):
        RangeMap = {
                2 : adxl.ADXL345_RANGE_2_G,
                4 : adxl.ADXL345_RANGE_4_G,
                8 : adxl.ADXL345_RANGE_8_G,
                16: adxl.ADXL345_RANGE_16_G
                }
        selRange = exactRange
        # TODO: add range ceil functionality to 2, 4, 8, 16
        self.imu.set_range(RangeMap[selRange])

    def getRange(self):
        return self.imu.get_range()

    def setDataRate(self, exactDataRate):
        DataRateMap = {
                0.1 : adxl.ADXL345_DATARATE_0_10_HZ,
                0.2 : adxl.ADXL345_DATARATE_0_20_HZ,
                0.39: adxl.ADXL345_DATARATE_0_39_HZ,
                0.78: adxl.ADXL345_DATARATE_0_78_HZ,
                1.56: adxl.ADXL345_DATARATE_1_56_HZ,
                3.13: adxl.ADXL345_DATARATE_3_13_HZ,
                6.25: adxl.ADXL345_DATARATE_6_25HZ,
                12.5: adxl.ADXL345_DATARATE_12_5_HZ,
                25  : adxl.ADXL345_DATARATE_25_HZ,
                50  : adxl.ADXL345_DATARATE_50_HZ,
                100 : adxl.ADXL345_DATARATE_100_HZ,
                200 : adxl.ADXL345_DATARATE_200_HZ,
                400 : adxl.ADXL345_DATARATE_400_HZ,
                800 : adxl.ADXL345_DATARATE_800_HZ,
                1600: adxl.ADXL345_DATARATE_1600_HZ,
                3200: adxl.ADXL345_DATARATE_3200_HZ
                }
        selDataRate = exactDataRate
        # TODO: Add rounding
        self.imu.set_data_rate(DataRateMap[selDataRate])
    
    def getDataRate(self):
        return self.imu.get_data_rate()

    def getAccels(self):
        # TODO: Incorporate Adafruit_ADXL345 docstring
        # TODO: Calibrate
        raw_accels = self.imu.read()
        # All g-range when FULL_RES = 1  3.9 mG/LSB
        # Need to add checking for 10 bit mode 2, 4 , 8, 16G modes
        _xoffset, _yoffset, _zoffset = 0, 0, 0
        offsets = (_xoffset, _yoffset, _zoffset)
        accelsG = [ raw_accel*0.00390625+offset for raw_accel, offset in zip(raw_accels, offsets) ]
        return accelsG

    def getRates(self):
        '''
        No Gyro's Present on ADXL345
        '''
        return (None, None, None)

