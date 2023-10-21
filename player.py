import math

import pygame


class Player:
    def __init__(self, screen: pygame.Surface, size: int):
        self.screen = screen
        self.center = {"x": self.screen.get_width() / 2,
                       "y": self.screen.get_height() / 2}
        self.size = size
        self.rotation_degrees = math.pi / 2
        self.head = {"x": self.center["x"] + (math.cos(self.rotation_degrees) * self.size),
                     "y": self.center["y"] + (-1 * (math.sin(self.rotation_degrees) * self.size))}

    def draw_player(self) -> pygame.Rect:
        Player.__movement_controller(self)
        player_width = 2

        player_left_degrees = self.rotation_degrees + ((5 * math.pi) / 6)
        player_right_degrees = self.rotation_degrees + ((7 * math.pi) / 6)

        player_left = {"x": self.center["x"] + (math.cos(player_left_degrees) * self.size),
                       "y": self.center["y"] + (-1 * (math.sin(player_left_degrees) * self.size))}

        player_right = {"x": self.center["x"] + (math.cos(player_right_degrees) * self.size),
                        "y": self.center["y"] + (-1 * (math.sin(player_right_degrees) * self.size))}

        player = pygame.draw.lines(self.screen, color="white", closed=True,
                                   points=[(player_left["x"], player_left["y"]),
                                           (self.center["x"], self.center["y"]),
                                           (player_right["x"], player_right["y"]),
                                           (self.head["x"], self.head["y"])],
                                   width=player_width)

        return player

    def __movement_controller(self):
        keys = pygame.key.get_pressed()

        Player.__rotate_player(self, keys)
        Player.__move_forward(self, keys)

    def __rotate_player(self, keys):
        rotation_speed = 10

        if keys[pygame.K_RIGHT]:
            self.rotation_degrees = self.rotation_degrees - math.radians(rotation_speed)
            self.head["x"] = self.center["x"] + (math.cos(self.rotation_degrees) * self.size)
            self.head["y"] = self.center["y"] + (-1 * math.sin(self.rotation_degrees) * self.size)

        if keys[pygame.K_LEFT]:
            self.rotation_degrees = self.rotation_degrees + math.radians(rotation_speed)
            self.head["x"] = self.center["x"] + (math.cos(self.rotation_degrees) * self.size)
            self.head["y"] = self.center["y"] + (-1 * math.sin(self.rotation_degrees) * self.size)

    def __move_forward(self, keys):
        velocity = 2

        if keys[pygame.K_UP]:
            self.center["x"] = self.center["x"] + (math.cos(self.rotation_degrees) * velocity)
            self.center["y"] = self.center["y"] + (-1 * math.sin(self.rotation_degrees) * velocity)
            self.head["x"] = self.center["x"] + (math.cos(self.rotation_degrees) * self.size)
            self.head["y"] = self.center["y"] + (-1 * math.sin(self.rotation_degrees) * self.size)
