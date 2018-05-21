class Motors():
    def __init__(self):
        self._m0 = 0
        self._m1 = 0

    @property
    def m0(self) -> float:
        '''
        Gets the value of motor 0
        :returns: returns value of motor 0
        '''
        return self._m0

    @m0.setter()
    def m0(self, power: float) -> None:
        '''
        Sets the value of motor 0
        :param power: Power as a percent
        '''
        self._m0 = power

    @property
    def m1(self) -> float:
        '''
        Gets the value of motor 1
        :returns: returns value of motor 1
        '''
        return self._m1

    @m1.setter()
    def m1(self, power: float) -> None:
        '''
        Sets the value of motor 1
        :param power: Power as a percent
        '''
        self._m1 = power
