from cilantro import Robot, UltrasoundSensor, LineSensor
from time import sleep

# Create instance of robot
robot = Robot()

sensor = UltrasoundSensor(trigger=17,echo=18)
line_sensor = LineSensor(pin=25)

while True:
    # Go forward for 3 seconds then stop
    robot.motors.m0 = 20
    robot.motors.m1 = 20
    sleep(3)
    robot.motors.m0 = 0
    robot.motors.m1 = 0
    sleep(1)