#!/usr/bin/env python3

import time
from ev3dev2.motor import OUTPUT_B, OUTPUT_D, SpeedPercent
from ev3dev2.motor import MoveSteering as PickwickCar
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import InfraredSensor
from ev3dev2.sensor import INPUT_4
from ev3dev2.sensor.lego import ColorSensor

pickwickCar = PickwickCar(OUTPUT_B, OUTPUT_D)
color_sensor = ColorSensor(INPUT_4)


def follow_line():
    pickwickCar.on(calculate_steering(), SpeedPercent(20))


def calculate_steering():
    # Read the reflection value
    reflection = color_sensor.reflected_light_intensity

    # Calculate the steering value
    steering = (55 - reflection) * 3
    if steering > 100:
        steering = 100
    if steering < -100:
        steering = -100
    print(steering)
    return steering
        

while True:
    follow_line()
    time.sleep(0.03)
