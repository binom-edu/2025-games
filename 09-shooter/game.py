import pygame
import random
import os


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_dir, 'playerShip.png'))
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 30
        self.hp = 100
        self.lives = 3
        self.shoot_delay = 1000
        self.last_shoot = pygame.time.get_ticks()
    def update(self):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -= 2
            if self.rect.left < 0: self.rect.left = 0
        if key_pressed[pygame.K_RIGHT]:
            self.rect.right = min(WIDTH, self.rect.right + 2)
        if key_pressed[pygame.K_SPACE]:
            self.shoot()
    
    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot > self.shoot_delay:
            Bullet(self.rect.centerx, self.rect.top)
            self.last_shoot = now
            bullet_snd.play()

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice(meteors_img)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * 0.7 / 2)
        self.rect.centerx = random.randrange(0, WIDTH)
        self.rect.centery = random.randrange(-100, 0)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(1, 10)
        all_sprites.add(self)
        mobs.add(self)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.rect.centerx = random.randrange(0, WIDTH)
            self.rect.centery = random.randrange(-100, 0)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(1, 10)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10
        all_sprites.add(self)
        bullets.add(self)
    def update(self):
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, coord):
        pygame.sprite.Sprite.__init__(self)
        self.image = explosion_anim[0]
        self.rect = self.image.get_rect()
        self.rect.center = coord
        all_sprites.add(self)
        self.frame = 0
        self.animation_rate = 50
        self.last_update = pygame.time.get_ticks()
        random.choice(expl_snd).play()

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(explosion_anim):
                self.kill()
            else:
                self.image = explosion_anim[self.frame]

def draw_hp(hp, surf):
    outlined_rect = pygame.Rect(20, 20, 100, 20)
    filled_rect = pygame.Rect(20, 20, hp, 20)
    pygame.draw.rect(surf, (0, 255, 0), filled_rect)
    pygame.draw.rect(surf, (255, 255, 255), outlined_rect, 2)

def draw_lives(lives, surf):
    image = pygame.image.load(os.path.join(img_dir, 'playerShip.png'))
    image = pygame.transform.scale(image, (30, 20))
    rect = image.get_rect()
    rect.top = 20
    for i in range(lives):
        rect.right = WIDTH - 20 - 35*i
        surf.blit(image, rect)


WIDTH = 400
HEIGHT = 600
FPS = 60

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Shooter 26')
clock = pygame.time.Clock()
img_dir = os.path.join(os.path.dirname(__file__), 'img')
bullet_img = pygame.image.load(os.path.join(img_dir, 'laserBlue16.png'))
meteors_img = []
meteors_list = os.listdir(os.path.join(img_dir, 'meteors'))
for filename in meteors_list:
    meteors_img.append(pygame.image.load(os.path.join(img_dir, 'meteors', filename)))
explosion_anim = []
for i in range(9):
    filename = f'regularExplosion0{i}.png'
    img = pygame.image.load(os.path.join(img_dir, 'explosions', filename))
    explosion_anim.append(pygame.transform.scale(img, (75, 75)))

snd_dir = os.path.join(os.path.dirname(__file__), 'snd')
bullet_snd = pygame.mixer.Sound(os.path.join(snd_dir, 'sfx_laser2.ogg'))
expl_snd = []
for filename in 'expl3.wav', 'expl6.wav':
    snd = pygame.mixer.Sound(os.path.join(snd_dir, filename))
    snd.set_volume(0.3)
    expl_snd.append(snd)
player_expl_snd = pygame.mixer.Sound(os.path.join(snd_dir, 'rumble1.ogg'))
pygame.mixer.music.load(os.path.join(snd_dir, 'bgmusic.mp3'))
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for i in range(5): Mob()

game_on = True
while game_on:
    clock.tick(FPS)
    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
    # обновление
    all_sprites.update()

    # столкновение игрока с метеоритом
    for hit in pygame.sprite.spritecollide(player, mobs, 1, pygame.sprite.collide_circle):
        Mob()
        player.hp -= hit.radius
        if player.hp <= 0:
            player.hp = 0
    
    # столкновение пули с метеоритом
    for hit in pygame.sprite.groupcollide(mobs, bullets, True, True):
        Explosion(hit.rect.center)
        Mob()

    if player.hp == 0:
        if player.lives > 1:
            player.lives -= 1
            player.hp = 100
        else:
            player_expl_snd.play()
            Explosion(player.rect.center)
            game_on = False

    # отрисовка
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    draw_hp(player.hp, screen)
    draw_lives(player.lives, screen)
    pygame.display.flip()

pygame.time.delay(2000)
pygame.quit()