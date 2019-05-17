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
        # TODO: Calibrate
        raw_accels = self.imu.read()
        # All g-range when FULL_RES = 1  3.9 mG/LSB
        # Need to add checking for 10 bit mode 2, 4 , 8, 16G modes
        _xoffset, _yoffset, _zoffset = 0, 0, 0
        offsets = (_xoffset, _yoffset, _zoffset)
        accelsG = [ raw_accel*0.00390625+offset for raw_accel, offset in zip(raw_accels, offsets) ]
        return accelsG

    @doc_inherit
    def getRates(self):
        '''
        No Gyro's Present on ADXL345
        '''
        return (None, None, None)

