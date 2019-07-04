from cilantro import Robot, UltrasoundSensor, LineSensor
from time import sleep

# Create instance of robot
robot = Robot()

# Go forward for 3 seconds then stop
robot.motors.m0 = 20
robot.motors.m1 = 20
sleep(3)
robot.motors.m0 = 0
robot.motors.m1 = 0

sensor = UltrasoundSensor(trigger=17,echo=18)
line_sensor = LineSensor(pin=25)

while True:
    print("Ultrasound", sensor.get_distance())
    print("On a line", line_sensor.on_line)
    sleep(1)
    if sensor.get_distance() < 5:
        # Something is less than 5 cm away, better stop
        robot.motors.m0 = 0
        robot.motors.m1 = 0
