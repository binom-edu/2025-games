import pygame


class Pers(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((10, 10))
        self.image.fill((255, 255, 0))

pygame.init()

screen = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Привет мир')

clock = pygame.time.Clock()

FPS = 30

pers = Pers()
game_on = True

while game_on:
    clock.tick(FPS)
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    # update

    # render
    screen.blit(pers.image, (300, 300))
    pygame.display.flip()

pygame.quit()