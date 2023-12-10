import pygame

from settings import player_color, resolution, fps


class Player(pygame.Rect):
    def __init__(self, game):
        self.game = game  # get main.py
        self.scale = (60, 10)
        self.speed = 400 / fps
        self.position = (resolution[0] // 2 - self.scale[0] // 2, resolution[1] - resolution[1] // 4)
        super().__init__(self.position, self.scale)

    def draw(self):
        pygame.draw.rect(self.game.screen, player_color, (self.position, self.scale), 5, 20)

    def _move(self):
        keys = pygame.key.get_pressed()
        x = self.position[0]  # cuz i have a tuple, i need crutch
        if keys[pygame.K_a] and self.position[0] > 0:
            x -= self.speed
        if keys[pygame.K_d] and self.position[0] + self.scale[0] < resolution[0]:
            x += self.speed
        self.position = (x, self.position[1])

    def get_rect(self):  # hitbox
        return pygame.Rect(self.position, self.scale)

    def _update(self):  # move and draw, ye
        self._move()
        self.draw()


if __name__ == '__main__':  # nevermind
    print(8 % 8 == 0)
