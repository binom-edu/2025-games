import pygame


class Pers(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((5, 5))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (300, 300)
    def update(self):
        self.rect.y += 1
    

pygame.init()
screen = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Игра с графикой')

clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()

FPS = 30

pers = Pers()
all_sprites.add(pers)

game_on = True
while game_on:
    # Обработка событий
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    
    # Обновление
    all_sprites.update()
    # Отрисовка
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()