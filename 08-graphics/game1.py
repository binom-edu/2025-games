import pygame


class Pers(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 300)
    
    def update(self):
        self.rect.y += 3
        if self.rect.bottom > 599:
            self.rect.bottom = 599

pygame.init()

screen = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Привет мир')

clock = pygame.time.Clock()

FPS = 30

all_sprites = pygame.sprite.Group()

pers = Pers()
all_sprites.add(pers)

game_on = True

while game_on:
    clock.tick(FPS)
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    # update
    all_sprites.update()

    # render
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()