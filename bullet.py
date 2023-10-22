import pygame
import math


class Bullet:
    def __init__(self, screen: pygame.Surface, initial_x, initial_y, trajectory_radians):
        self.__screen = screen
        self.current_x = initial_x
        self.current_y = initial_y
        self.__trajectory_radians = trajectory_radians

    def fire(self):
        bullet_speed = 15
        self.current_x += (math.cos(self.__trajectory_radians) * bullet_speed)
        self.current_y += (-1 * math.sin(self.__trajectory_radians) * bullet_speed)

        center = (self.current_x, self.current_y)
        Bullet.__draw_bullet(self, center)

    def __draw_bullet(self, center):
        pygame.draw.circle(surface=self.__screen, color="white", center=center, radius=2, width=0)
