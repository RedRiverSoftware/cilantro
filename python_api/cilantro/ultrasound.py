from gpiozero import DistanceSensor


class UltraSoundSensor():
    def __init__(self, trigger: int, echo: int) -> None:
        self.sensor = DistanceSensor(trigger=trigger, echo=echo)

    def get_distance(self) -> float:
        '''
        Gets the distance of an object from the sensor in cm
        '''
        distance_in_cm = self.sensor.distance * 100
        return distance_in_cm
