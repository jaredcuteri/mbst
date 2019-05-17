from abc import ABC, abstractmethod

class AbstractIMU(ABC):
"""
AbstractIMU is an Abstract Base Class for IMU devices
"""
    def __init__(self,dataRateHz=200, dataRangeG=8):
        self.dataRateHz = dataRateHz
        self.dataRangeG = dataRangeG
        super().__init__()

    @abstractmethod
    def setRange(self):
        pass

    @abstractmethod
    def getRange(self):
        pass

    @abstractmethod
    def setDataRate(self):
        pass

    @abstractmethod
    def getDataRate(self):
        pass

    @abstractmethod
    def getAccels(self):
        pass

    @abstractmethod
    def getRates(self):
        pass
