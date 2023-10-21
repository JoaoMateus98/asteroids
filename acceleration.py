import pygame
from pygame import key
import math


class Acceleration:
    def __init__(self):
        self.__GOAL = math.atan(10) + (math.pi / 2)
        self.__ACCELERATION_SCALER = 3
        self.__current_acceleration = 0
        self.__MIN_DELTA_TIME = -5
        self.__MAX_DELTA_TIME = 5
        self.__delta_time = self.__MIN_DELTA_TIME
        self.__ship_current_velocity = 0

    def accelerate(self):

        if self.__delta_time <= self.__MAX_DELTA_TIME:
            self.__delta_time += 1 / 8
            self.__current_acceleration = math.atan(self.__delta_time) + (math.pi / 2)
            self.__ship_current_velocity = self.__current_acceleration * self.__ACCELERATION_SCALER

        return self.__ship_current_velocity

    def decelerate(self):
        if self.__delta_time == self.__MIN_DELTA_TIME:
            self.__ship_current_velocity = 0

        elif self.__delta_time >= self.__MIN_DELTA_TIME:
            self.__delta_time -= 1 / 8
            self.__current_acceleration = math.atan(self.__delta_time) + (math.pi / 2)
            self.__ship_current_velocity = self.__current_acceleration * self.__ACCELERATION_SCALER

        return self.__ship_current_velocity
