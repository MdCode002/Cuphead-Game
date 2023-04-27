import pygame
import random


pygame.init()

# classe qui vas gerer le projectile de notre class


class Projectile(pygame.sprite.Sprite):

    def __init__(self, Player, Right):
        super().__init__()
        self.velocity = random.randint(57, 60)
        self.Player = Player
        self.Right = Right

        self.current_frame = 0
        self.image = pygame.image.load("./assets/Arme/BNorm_1.png")
        self.image = pygame.transform.scale(self.image, (50, 20))
        self.rect = self.image.get_rect()
        if self.Right:
            self.rect.x = Player.rect.x+70
        else:
            self.rect.x = Player.rect.x-45
            self.image = pygame.transform.flip(self.image, True, False)
        self.rect.y = Player.rect.y+25+random.randint(1, 20)
        self.direction = "none"

    def move(self):
        if self.direction == "none" or self.direction == "Right":
            self.rect.x += self.velocity
            # Changer l'image affichée pour créer l'animation
            self.current_frame = (self.current_frame + 1) % len(Bullet)
            self.image = Bullet[self.current_frame]

            for monster in self.Player.game.check_collition(self, self.Player.game.all_ennemy):
                self.Player.all_Projectiles.remove(self)
                monster.damage(self.Player.attack)
            self.direction = "Right"

            # vérifier si le projectile est présent dans l'écran
            if self.rect.x > 1024 or self.Player.game.check_collition(self, self.Player.game.all_ennemy):
                self.Player.all_Projectiles.remove(self)

    def moveLeft(self):
        if self.direction == "none" or self.direction == "Left":
            self.rect.x -= self.velocity
            # Changer l'image affichée pour créer l'animation
            self.current_frame = (self.current_frame + 1) % len(Bullet)
            self.image = pygame.transform.flip(
                Bullet[self.current_frame], True, False)
            for monster in self.Player.game.check_collition(self, self.Player.game.all_ennemy):
                self.Player.all_Projectiles.remove(self)
                monster.damage(self.Player.attack)

            # vérifier si le projectile est présent dans l'écran
            if self.rect.x < 0 or self.Player.game.check_collition(self, self.Player.game.all_ennemy):

                self.Player.all_Projectiles.remove(self)
            self.direction = "Left"


Bullet = []
# Découpez la feuille de sprite en plusieurs images
for i in range(1, 8):
    image = pygame.image.load(
        f'./assets/Arme/BNorm_{i}.png')
    image = pygame.transform.scale(image, (50, 20))
    Bullet.append(image)
