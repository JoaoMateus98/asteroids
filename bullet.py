import pygame
import math


class Bullet:
    def __init__(self, screen: pygame.Surface, initial_pos: dict, trajectory_radians):
        self.__screen = screen
        self.current_pos = {"x": initial_pos["x"],
                            "y": initial_pos["y"]}
        self.__trajectory_radians = trajectory_radians

    def fire(self):
        bullet_speed = 10
        self.current_pos["x"] += (math.cos(self.__trajectory_radians) * bullet_speed)
        self.current_pos["y"] += (-1 * math.sin(self.__trajectory_radians) * bullet_speed)

        center = (self.current_pos["x"], self.current_pos["y"])
        Bullet.__draw_bullet(self, center)

    def __draw_bullet(self, center):
        pygame.draw.circle(surface=self.__screen, color="white", center=center, radius=2, width=0)
