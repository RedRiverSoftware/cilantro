from cilantro.motors import Motors


class Robot():
    def __init__(self):
        self.motors = Motors

    @staticmethod
    def _calc_ultrasound_distance(start_time: float, end_time: float) -> float:
        '''
        Calculates distance of an object using ultrasonic pulse times
        :param start_time: Pulse start time
        :param arg2: Pulse end time
        :return: return distance in centimetres
        '''
        duration = end_time - start_time
        distance = duration * 17150  # See footnote 1
        return distance


# Footnote 1:
# 343m/s is speed of sound at sea level, 17510 is that converted into cm's and
# divided by two as we only want distance to object not there and back
