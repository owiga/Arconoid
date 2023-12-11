import pygame, random

from settings import resolution, ball_color, fps, height, width


class Ball(pygame.Rect):
    direct = [1, -1]  # direction

    def __init__(self, game):
        self.game = game  # get main.py
        self.ingame = True
        self.win = False
        self.font = pygame.font.SysFont("ArialBlack", 50)
        self.text = self.font.render("GG, U LOST", True, "red")
        self.scale = (5, 5)
        self.speed = 150 / fps
        self.position = [resolution[0] // 2, resolution[1] // 2]
        self.hitbox = [self.position[0] - self.scale[0] // 2, self.position[1] - self.scale[0] // 2]  # cuz i have circle, i need get his square hitbox
        self.hitbox_scale = [self.scale[0] + 3, self.scale[0] + 3]
        self.direction = [random.choice(Ball.direct), 1]
        super().__init__(self.hitbox, self.hitbox_scale)

    def draw(self):
        if self.ingame:
            pygame.draw.circle(self.game.screen, ball_color, self.position, self.scale[0], 5)  # circle
        elif not self.win:
            text_x = width // 2 - self.text.get_width() // 2  # text "gg"
            text_y = height // 2 - self.text.get_height() // 2
            self.game.screen.blit(self.text, (text_x, text_y))
        elif self.win:
            self.text = self.font.render("You win!", True, "red")
            text_x = width // 2 - self.text.get_width() // 2  # text "gg"
            text_y = height // 2 - self.text.get_height() // 2
            self.game.screen.blit(self.text, (text_x, text_y))

    def _move(self):  # default move
        if self.ingame:
            self.hitbox[0] += self.speed * self.direction[0]
            self.hitbox[1] += self.speed * self.direction[1]
            self.position[0] += self.speed * self.direction[0]
            self.position[1] += self.speed * self.direction[1]

    def get_rect(self):  # get hitbox
        return pygame.Rect(self.hitbox, self.hitbox_scale)

    def _update(self):  # just update
        self._move()
        self.draw()
