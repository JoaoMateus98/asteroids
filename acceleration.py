import math


class Acceleration:
    def __init__(self):
        self.__GOAL = math.atan(10) + (math.pi / 2)
        self.__ACCELERATION_SCALER = 3
        self.__current_acceleration = 0
        self.__MIN_DELTA_TIME = -60
        self.__MAX_DELTA_TIME = 10
        self.__delta_time = self.__MIN_DELTA_TIME
        self.__ship_current_velocity = 0
        self.__stopped_accelerating = True

    def accelerate(self):
        if self.__stopped_accelerating is True:
            if self.__delta_time < -3:
                self.__delta_time = -3
            elif self.__delta_time > 5:
                self.__delta_time = -1
            elif self.__delta_time > 0:
                self.__delta_time = -3.5

        if self.__delta_time <= self.__MAX_DELTA_TIME:
            self.__delta_time += 1 / 8
            self.__current_acceleration = 1.2 * math.atan(self.__delta_time) + 1.865
            self.__ship_current_velocity = self.__current_acceleration * self.__ACCELERATION_SCALER

        self.__stopped_accelerating = False
        return self.__ship_current_velocity

    def decelerate(self):
        self.__stopped_accelerating = True

        if self.__delta_time == self.__MIN_DELTA_TIME:
            self.__ship_current_velocity = 0

        elif self.__delta_time >= self.__MIN_DELTA_TIME:
            self.__delta_time -= 1 / 8
            self.__current_acceleration = 1.2 * math.atan(self.__delta_time) + 1.865
            self.__ship_current_velocity = self.__current_acceleration * self.__ACCELERATION_SCALER

        return self.__ship_current_velocity
