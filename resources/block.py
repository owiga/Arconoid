import pygame, random

from settings import blocks_colors


class Block(pygame.Rect):
    def __init__(self, game, pos: tuple, scale: tuple, visibility: bool):
        self.position = pos
        self.scale = scale
        self.game = game  # get main.py
        self.color = random.choice(blocks_colors)
        self.Visibility = visibility  # visibility check
        super().__init__(self.position, self.scale)

    def draw(self):
        pygame.draw.rect(self.game.screen, "pink" if self.Visibility else "black", self)
