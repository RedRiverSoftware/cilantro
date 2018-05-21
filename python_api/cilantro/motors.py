from gpiozero import CamJamRobot
from typings import Optional


class Motors():
    def __init__(self):
        self._m0 = 0
        self._m1 = 0
        self._cam_jam_robot = CamJamRobot()

    @property
    def m0(self) -> int:
        '''
        Gets the value of Motor 0
        :returns: returns value of Motor 0
        '''
        return self._m0

    @m0.setter()
    def m0(self, power: int) -> None:
        '''
        Sets the value of Motor 0
        :param power: Power as a percent
        '''
        self._m0 = power
        self._update_power(power, m1=self._m1)

    @property
    def m1(self) -> int:
        '''
        Gets the value of Motor 1
        :returns: returns value of Motor 1
        '''
        return self._m1

    @m1.setter()
    def m1(self, power: int) -> None:
        '''
        Sets the value of Motor 1
        :param power: Power as a percent
        '''
        self._m1 = power
        self._update_power(power, m0=self._m0)

    def _update_power(self, power: int, m0: Optional[int] = None,
                      m1: Optional[int] = None) -> None:
        '''
        Sets the power of the motors. Either m0 or m1 *must* be specified
        :param power: Power motor is to be set to
        :param m0: power of Motor 0
        :param m1: power of Motor 1
        '''
        if m0 is None and m1 is None:
            raise ValueError("One of m0 or m1 must be specified")
        power_percent = power/100.0
        if m0:
            self._cam_jam_robot.value = (m0, power_percent)
        if m1:
            self._cam_jam_robot.value = (power, m1)
