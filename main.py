import pygame
import sys

from settings import resolution, fps, newGame_cooldown
from level import map
from resources.player import Player
from resources.block import Block
from resources.ball import Ball


class Game:
    player: Player
    ball: Ball

    def __init__(self):
        self.blocks = []  # our map here
        self.newGameEvent = pygame.USEREVENT
        pygame.init()
        self.stepY = 0
        self.stepX = 0
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.entity()

    def entity(self):  # initialization of ball, player, etc
        self.player = Player(self)
        for index, text in enumerate(map):
            if index % 8 == 0 and index != 0:
                self.stepY += 40
                self.stepX = 0
            if text == 'a':
                self.blocks.append(Block(self, (5 + 75 * self.stepX, 5 + self.stepY), (65, 30), True))
                self.stepX += 1
            elif text == '_':
                self.blocks.append(Block(self, (5 + 75 * self.stepX, 5 + self.stepY), (65, 30), False))
                self.stepX += 1
        self.ball = Ball(self)

    def update(self):  # movement and etc
        self.screen.fill("black")
        self.player._update()
        for block in self.blocks:
            block.draw()
            if self.ball.get_rect().colliderect(block) and block.Visibility:
                if self.ball.position[0] < block.left or self.ball.position[0] > block.right:
                    self.ball.direction[0] *= -1
                    self.blocks.remove(block)
                else:
                    self.ball.direction[1] *= -1
                    self.blocks.remove(block)
        pygame.display.set_caption(f'{self.clock.get_fps(): .1f}')
        self.ball._update()  # ball below cuz it would superimposed on the top  blocks

    def check_collide(self):
        if self.ball.position[0] - self.ball.scale[0] < 1:  # wall collide
            self.ball.direction[0] *= -1
        elif self.ball.position[0] + self.ball.scale[0] > resolution[0] - 1:  # wall collide
            self.ball.direction[0] *= -1
        elif self.ball.position[1] - self.ball.scale[1] < 1:  # wall collide
            self.ball.direction[1] *= -1
        if self.ball.get_rect().colliderect(self.player.get_rect()):  # player collide !important!
            self.ball.direction[1] *= -1
        # pass

    def check_events(self):  # default checking
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == self.newGameEvent:
                self.restart()
                pygame.time.set_timer(self.newGameEvent, 0)
        pygame.display.flip()
        self.clock.tick(fps)

    def check_lose(self):  # lose checker, !important!
        if self.ball.position[1] > resolution[1]:
            self.ball.ingame = False
            pygame.time.set_timer(self.newGameEvent, newGame_cooldown)
            self.ball.position[1] = 0

    def run(self):  # main loop
        while True:
            self.check_lose()
            self.check_events()
            self.check_collide()
            self.update()

    def restart(self):  # just restart xd
        self.blocks = []
        self.stepY = 0
        self.stepX = 0
        self.screen = pygame.display.set_mode(resolution)
        self.clock = pygame.time.Clock()
        self.entity()


if __name__ == '__main__':  # start
    game = Game()
    game.run()
