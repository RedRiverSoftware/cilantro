from cilantro import Robot, UltrasoundSensor, LineSensor
from time import sleep

# Create instance of robot
robot = Robot()

robot.motors.m0 = 30
robot.motors.m1 = 30

sensor = UltrasoundSensor(trigger=17,echo=18)
line_sensor = LineSensor(pin=25)

left = True
turning = False

while True:
    if sensor.get_distance() < 30:
        if not turning:
            turning = True
            if left:
                left = False
                robot.motors.m1 = 0
            else:
                left = True
                robot.motors.m0 = 0
    else:
        turning = False
        robot.motors.m0 = 30
        robot.motors.m1 = 30
