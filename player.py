import math
import pygame
from bullet import Bullet


class Player:
    def __init__(self, screen: pygame.Surface, size: int):
        self.screen = screen
        self.x = self.screen.get_width() / 2
        self.y = self.screen.get_height() / 2
        self.dx = 0
        self.dy = 0

        self.size = size
        self.rotation_radians = math.pi / 2
        self.head_x = self.x + (math.cos(self.rotation_radians) * self.size)
        self.head_y = self.y + (-1 * (math.sin(self.rotation_radians) * self.size))

        self.was_firing = False
        self.fired_bullets = []

    def draw_player(self) -> pygame.Rect:
        Player.__stay_in_screen(self)
        Player.__movement_controller(self)
        player_width = 2

        player_left_degrees = self.rotation_radians + ((5 * math.pi) / 6)
        player_right_degrees = self.rotation_radians + ((7 * math.pi) / 6)

        player_left_x = self.x + (math.cos(player_left_degrees) * self.size)
        player_left_y = self.y + (-1 * (math.sin(player_left_degrees) * self.size))
        player_right_x = self.x + (math.cos(player_right_degrees) * self.size)
        player_right_y = self.y + (-1 * (math.sin(player_right_degrees) * self.size))

        player = pygame.draw.lines(self.screen, color="white", closed=True,
                                   points=[(player_left_x, player_left_y),
                                           (self.x, self.y),
                                           (player_right_x, player_right_y),
                                           (self.head_x, self.head_y)],
                                   width=player_width)

        return player

    def __movement_controller(self):
        # normalize the radians
        if self.rotation_radians > (math.pi * 2):
            self.rotation_radians = 0
        if self.rotation_radians < 0:
            self.rotation_radians = (math.pi * 2)

        keys = pygame.key.get_pressed()

        Player.__bullet_controller(self, keys)
        Player.__rotate_player(self, keys)
        Player.__move_forward(self, keys)

    def __stay_in_screen(self):
        if self.x < 0:
            self.x = self.screen.get_width()
        if self.x > self.screen.get_width():
            self.x = 0

        if self.y < 0:
            self.y = self.screen.get_height()
        if self.y > self.screen.get_height():
            self.y = 0

    def __bullet_controller(self, keys):
        for index, bullet in enumerate(self.fired_bullets):
            bullet.fire()
            if (bullet.current_x > self.screen.get_width() or bullet.current_x < 0 or
                    bullet.current_y > self.screen.get_height() or bullet.current_y < 0):
                self.fired_bullets.pop(index)

        if not self.was_firing:
            if keys[pygame.K_SPACE]:
                Player.__fire(self)

        if keys[pygame.K_SPACE]:
            self.was_firing = True
        else:
            self.was_firing = False

    def __fire(self):
        bullet = Bullet(self.screen, self.head_x, self.head_y, self.rotation_radians)
        self.fired_bullets.append(bullet)

    def __rotate_player(self, keys):
        rotation_speed = 3.5

        if keys[pygame.K_RIGHT]:
            self.rotation_radians = self.rotation_radians - math.radians(rotation_speed)
            self.head_x = self.x + (math.cos(self.rotation_radians) * self.size)
            self.head_y = self.y + (-1 * math.sin(self.rotation_radians) * self.size)

        if keys[pygame.K_LEFT]:
            self.rotation_radians = self.rotation_radians + math.radians(rotation_speed)
            self.head_x = self.x + (math.cos(self.rotation_radians) * self.size)
            self.head_y = self.y + (-1 * math.sin(self.rotation_radians) * self.size)

    def __move_forward(self, keys):
        self.x += self.dx
        self.y += self.dy

        if keys[pygame.K_UP]:
            Player.accelerate(self)
        else:
            Player.decelerate(self)

        self.head_x = self.x + (math.cos(self.rotation_radians) * self.size)
        self.head_y = self.y + (-1 * math.sin(self.rotation_radians) * self.size)

    def accelerate(self):
        acceleration_scale = .3

        if abs(self.dx) < 10:
            self.dx += math.cos(self.rotation_radians) * acceleration_scale
        if abs(self.dy) < 10:
            self.dy += (-1 * math.sin(self.rotation_radians)) * acceleration_scale

    def decelerate(self):

        if -.1 < self.dx < .1:
            self.dx = 0
        elif self.dx < .1:
            self.dx += .05
        elif self.dx > .1:
            self.dx -= .05
        if -.1 < self.dy < .1:
            self.dy = 0
        elif self.dy < .1:
            self.dy += .05
        elif self.dy > .1:
            self.dy -= .05
