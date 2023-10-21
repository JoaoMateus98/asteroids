import math
import pygame
from acceleration import Acceleration


class Player:
    def __init__(self, screen: pygame.Surface, size: int):
        self.screen = screen
        self.center = {"x": self.screen.get_width() / 2,
                       "y": self.screen.get_height() / 2}
        self.size = size
        self.rotation_radians = math.pi / 2
        self.head = {"x": self.center["x"] + (math.cos(self.rotation_radians) * self.size),
                     "y": self.center["y"] + (-1 * (math.sin(self.rotation_radians) * self.size))}

        self.acceleration_module = Acceleration()
        self.rotation_radians_during_acceleration = self.rotation_radians
        self.velocity = 0

    def draw_player(self) -> pygame.Rect:
        Player.__movement_controller(self)
        player_width = 2

        player_left_degrees = self.rotation_radians + ((5 * math.pi) / 6)
        player_right_degrees = self.rotation_radians + ((7 * math.pi) / 6)

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
        # normalize the radians
        if self.rotation_radians > (math.pi * 2):
            self.rotation_radians = 0
        if self.rotation_radians < 0:
            self.rotation_radians = (math.pi * 2)

        keys = pygame.key.get_pressed()

        Player.__rotate_player(self, keys)
        Player.__move_forward(self, keys)

    def __rotate_player(self, keys):
        rotation_speed = 10

        if keys[pygame.K_RIGHT]:
            self.rotation_radians = self.rotation_radians - math.radians(rotation_speed)
            self.head["x"] = self.center["x"] + (math.cos(self.rotation_radians) * self.size)
            self.head["y"] = self.center["y"] + (-1 * math.sin(self.rotation_radians) * self.size)

        if keys[pygame.K_LEFT]:
            self.rotation_radians = self.rotation_radians + math.radians(rotation_speed)
            self.head["x"] = self.center["x"] + (math.cos(self.rotation_radians) * self.size)
            self.head["y"] = self.center["y"] + (-1 * math.sin(self.rotation_radians) * self.size)

    def __move_forward(self, keys):

        if keys[pygame.K_UP]:
            self.velocity = self.acceleration_module.accelerate()

            self.center["x"] = self.center["x"] + (math.cos(self.rotation_radians) * self.velocity)
            self.center["y"] = self.center["y"] + (-1 * math.sin(self.rotation_radians) * self.velocity)

            # record last radians so ship keeps the same momentum during deceleration
            self.rotation_radians_during_acceleration = self.rotation_radians
        else:
            self.velocity = self.acceleration_module.decelerate()

            self.center["x"] = self.center["x"] + (math.cos(self.rotation_radians_during_acceleration) * self.velocity)
            self.center["y"] = (self.center["y"] +
                                (-1 * math.sin(self.rotation_radians_during_acceleration) * self.velocity))

        self.head["x"] = self.center["x"] + (math.cos(self.rotation_radians) * self.size)
        self.head["y"] = self.center["y"] + (-1 * math.sin(self.rotation_radians) * self.size)

        print(self.velocity)
