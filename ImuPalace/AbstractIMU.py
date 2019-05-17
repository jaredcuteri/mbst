from abc import ABC, abstractmethod

class AbstractIMU(ABC):
    """
    AbstractIMU is an Abstract Base Class for IMU devices
    """
    # TODO: Does this close the door on addt'l derived kwargs?
    def __init__(self,dataRateHz=200, dataRangeG=8):
        self.dataRateHz = dataRateHz
        self.dataRangeG = dataRangeG
        super().__init__()

    @abstractmethod
    def setRange(self):
        '''
        Set Range [+/- G's] of measurements
        '''
        pass

    @abstractmethod
    def getRange(self):
        '''
        Get Range [+/- G's] of measurements
        '''
        pass

    @abstractmethod
    def setDataRate(self):
        '''
        Set Data Rate [Hz] of measurements
        '''
        pass

    @abstractmethod
    def getDataRate(self):
        '''
        Get Data Rate [Hz] of measurements
        '''
        pass

    @abstractmethod
    def getAccels(self):
        '''
        Get Acceleration [G] measurement tuple (x, y, z)
        '''
        pass

    @abstractmethod
    def getRates(self):
        '''
        Get Angular Rates [deg/s] measurement tuple (x, y, z)
        '''
        pass
