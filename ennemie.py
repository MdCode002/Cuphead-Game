import pygame
import random
# import animation
pygame.init()


class Ennemy(pygame.sprite.Sprite):
    def __init__(self, game, nom):

        super().__init__()
        self.nom = nom
        self.game = game
        self.health = 50
        self.max_health = 100
        self.velocity = random.randint(6, 10)
        self.attack = 10
        self.image = pygame.image.load(
            f"./assets/Ennemy/flowergrunt_run_0001.png")
        self.image = pygame.transform.scale(self.image, (95, 130))
        self.rect = self.image.get_rect()
        self.rect.x = 600 + random.randint(0, 300)
        self.rect.y = 370
        self.curentframe = 0
        self.curentframeD = 0

    def damage(self, amount):
        # infliger les degat
        self.health -= amount
        # on verifie si pv < 0
        # if self.health <= 0:
        # faire reapparaitre le monstre

        # def updateAnimation(self):
        #     self.animate()

    def update_health_bar(self, surface):

        # dessiner notre bar de vie
        pygame.draw.rect(surface,  (60, 63, 63), [
                         self.rect.x, self.rect.y-7, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [
                         self.rect.x, self.rect.y-7, self.health, 7])

    def forward(self):
        # le deplaemnt ne se fait que i il n'y a pas de colistion sur un joueur
        if not self.game.check_collition(self, self.game.all_player):
            self.rect.x -= self.velocity
        if self.rect.x < 2:
            self.rect.x = 600 + random.randint(0, 300)

    def animateEnimie(self, gameE):
        if self.health > 0:
            if self.curentframe > len(flowerguntimgs)-1:
                self.curentframe = 0
                self.image = flowerguntimgs[self.curentframe]
            else:
                self.image = flowerguntimgs[self.curentframe]
            self.curentframe += 1
        else:
            if self.curentframeD > len(flowerguntimgsDead)-1:
                self.rect.x = 600 + random.randint(0, 300)
                self.velocity = random.randint(2, 4)
                self.health = self.max_health
                self.curentframeD = 0
            else:
                self.image = flowerguntimgsDead[self.curentframeD]
                self.curentframeD += 1


flowerguntimgs = []
flowerguntimgsDead = []
for i in range(1, 17):

    if i > 9:
        imageE = pygame.image.load(
            f"./assets/Ennemy/flowergrunt_run_00{i}.png")
        imageE = pygame.transform.scale(imageE, (75, 120))
    else:
        imageE = pygame.image.load(
            f"./assets/Ennemy/flowergrunt_run_000{i}.png")
        imageE = pygame.transform.scale(imageE, (75, 120))

    flowerguntimgs.append(imageE)
for i in range(1, 11):

    imageED = pygame.image.load(
        f"./assets/Ennemy/Dead{i}.png")
    imageED = pygame.transform.scale(imageED, (125, 130))

    flowerguntimgsDead.append(imageED)


class flowergunt(Ennemy):
    def __init__(self, game):
        super().__init__(game, "flowergunt")
