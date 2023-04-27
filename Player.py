import time
import pygame
from Arme import Projectile
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.pvimgs = []
        for i in range(0, 4):
            image = pygame.image.load(
                f'./assets/Player/{i}.png')
            self.pvimgs.append(image)
        self.health = 3
        self.max_health = 3
        self.all_Projectiles = pygame.sprite.Group()
        self.attack = 5
        self.game = game
        self.velocity = 35
        self.image = pygame.image.load(
            "./assets/Player/idle/cuphead_idle_0001.png")
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 370
        self.pvimg = self.pvimgs[self.health]
        self.pvrect = self.pvimg.get_rect()
        self.pvrect.x = 10
        self.pvrect.y = 530
        self.time_last_colistion = time.monotonic()-4
        self.Right = True
        self.is_jumping = False
        self.jumpGravity = 10
        self.jump_height = 60
        self.jump_Velocity = self.jump_height

    def Lancer_Projectile(self):
        if self.Right:
            self.all_Projectiles.add(Projectile(self, True))
        else:
            self.all_Projectiles.add(Projectile(self, False))

    def moveRight(self):
        # si le joueur n'est pas en colision
        if not self.game.check_collition(self, self.game.all_ennemy):
            self.rect.x += self.velocity
            self.Right = True

    def PlayerJump(self):
        self.rect.y -= self.jump_Velocity
        self.jump_Velocity -= self.jumpGravity
        if self.jump_Velocity < - self.jump_height:
            self.jump_Velocity = self.jump_height
            self.is_jumping = False

    def moveLeft(self):
        if not self.game.check_collition(self, self.game.all_ennemy):
            self.Right = False
            self.rect.x -= self.velocity


def Player_ImgLoader():
    # stocker  les image idle
    player_idle = []
    player_idleLeft = []
    hit = []
    Shoot = []
    ShootLeft = []
    run = []
    runRev = []
    Jump = []
    JumpRev = []
    RunShoot = []
    # Charger les image les image idle
    for i in range(1, 6):
        playerimg = pygame.image.load(
            f"./assets/Player/idle/cuphead_idle_000{i}.png")
        playerimg = pygame.transform.scale(playerimg, (65, 95))
        playerigleft = pygame.transform.flip(playerimg, True, False)
        player_idle.append(playerimg)
        player_idleLeft.append(playerigleft)

    player_idleRight = player_idle
    # Charger les image de shoot
    for i in range(1, 4):
        shootimg = pygame.image.load(
            f"./assets/Player/idle/cuphead_shoot_straight_000{i}.png")
        shootimg = pygame.transform.scale(shootimg, (85, 95))

        Shoot.append(shootimg)

    # Charger les image de course
    for i in range(1, 10):
        runimg = pygame.image.load(
            f"./assets/Player/run/cuphead_run_000{i}.png")
        runimg = pygame.transform.scale(runimg, (85, 95))
        runimgRE = pygame.transform.flip(runimg, True, False)
        run.append(runimg)
        runRev.append(runimgRE)

    # Charger les image de course
    for i in range(1, 9):
        jumpimg = pygame.image.load(
            f"./assets/Player/Jump/cuphead_jump_000{i}.png")
        jumpimg = pygame.transform.scale(jumpimg, (65, 75))
        jumpimgRE = pygame.transform.flip(jumpimg, True, False)
        Jump.append(jumpimg)
        JumpRev.append(jumpimgRE)
    # Charger les image du run en tirant

    for i in range(1, 17):
        if i > 9:
            imageE = pygame.image.load(
                f"./assets/RunShoot/cuphead_run_shoot_00{i}.png")
            imageE = pygame.transform.scale(imageE, (85, 95))
        else:
            imageE = pygame.image.load(
                f"./assets/RunShoot/cuphead_run_shoot_000{i}.png")
            imageE = pygame.transform.scale(imageE, (85, 95))

        RunShoot.append(imageE)
    for i in range(1, 7):

        imageH = pygame.image.load(
            f"./assets/Player/hit/cuphead_hit_000{i}.png")
        imageH = pygame.transform.scale(imageE, (85, 95))

        hit.append(imageH)

    current_frame = 0
    current_frame_Shoot = 0
    current_frame_Jump = 0
    current_frame_run = 0
    current_frame_runShoot = 0
    frame_imag_hit = 0
    return player_idle, player_idleLeft, player_idleRight, Shoot, ShootLeft, run, runRev, current_frame, current_frame_Shoot, current_frame_run, Jump, JumpRev, current_frame_Jump, current_frame_runShoot, RunShoot, frame_imag_hit, hit
