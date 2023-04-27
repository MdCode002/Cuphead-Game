import pygame
from Player import Player
from ennemie import Ennemy, flowergunt
from Arme import Projectile
from Player import Player_ImgLoader
import pygame.mixer
# J'importe les Image du player

pygame.init()


class Game():

    def __init__(self):
        self.all_player = pygame.sprite.Group()
        self.Player = Player(self)
        self.all_player.add(self.Player)

        self.son = pygame.mixer.Sound(
            './assets/son/Cuphead-Menu-Original-Theme-Song.mp3')

        # groupe de monstre
        self.all_ennemy = pygame.sprite.Group()
        self.pressed = {}
        self.is_Playing = False

    def game_start(self):
        self.spawn_Ennemy(flowergunt)
        self.spawn_Ennemy(flowergunt)

        # self.spawn_Ennemy()
        self.is_Playing = True

    def game_over(self):
        self.all_ennemy = pygame.sprite.Group()
        self.Player.health = self.Player.max_health
        self.son.play(loops=-1)
        self.fpsTitle = 0
        self.is_Playing = False

    def update(self, game, screen, player_idle, player_idleLeft, player_idleRight, Shoot, ShootLeft, run, runRev, current_frame, current_frame_Shoot, current_frame_run):
        # game.Player.update_health_bar(screen)
        screen.blit(game.Player.pvimg, game.Player.pvrect)

        # Pour Courire vers la droite
        if game.pressed.get(pygame.K_RIGHT) and not game.pressed.get(pygame.K_LEFT):
            screen.blit(run[current_frame_run], game.Player.rect)
            current_frame_run = (current_frame_run + 1) % len(run)
            player_idle = player_idleRight
            if game.Player.rect.x < 880:
                game.Player.moveRight()

            # Pour Courire vers la Gauche
        if game.pressed.get(pygame.K_LEFT) and not game.pressed.get(pygame.K_RIGHT):
            screen.blit(runRev[current_frame_run], game.Player.rect)
            current_frame_run = (current_frame_run + 1) % len(runRev)
            player_idle = player_idleLeft
            if game.Player.rect.x > 60:
                game.Player.moveLeft()
        # On definit si le projectile vas ver la droite ou vers la gauche
        for projectile in game.Player.all_Projectiles:
            if Projectile.direction == "none":
                if player_idle == player_idleRight:

                    projectile.move()
                else:
                    projectile.moveLeft()
            elif Projectile.direction == "Right":
                projectile.move()
            elif Projectile.direction == "Left":
                projectile.moveLeft()

        # Lancer Projectile et Animation Idle du player
        if game.pressed.get(pygame.K_z):
            # Lancer le projectile
            game.Player.Lancer_Projectile()
            # idle vers la gauche
            if player_idle == player_idleLeft:
                tmp = pygame.transform.flip(
                    Shoot[current_frame_Shoot], True, False)
                screen.blit(tmp, game.Player.rect)
                current_frame_Shoot = (current_frame_Shoot + 1) % len(Shoot)
            # idle vers la droite
            else:
                screen.blit(Shoot[current_frame_Shoot], game.Player.rect)
                current_frame_Shoot = (current_frame_Shoot + 1) % len(Shoot)
            # recuperer les projectile du joueur

        elif (not game.pressed.get(pygame.K_RIGHT) and not game.pressed.get(pygame.K_LEFT)) or (game.pressed.get(pygame.K_RIGHT) and game.pressed.get(pygame.K_LEFT)):
            game.Player.image = player_idle[current_frame]
            screen.blit(game.Player.image, game.Player.rect)
            current_frame = (current_frame + 1) % len(player_idle)

        for monster in game.all_ennemy:
            monster.forward()
            # monster.update_health_bar(screen)

        game.Player.all_Projectiles.draw(screen)

        # appliquer l'ensemble des image de mon groupe d'enemy
        game.all_ennemy.draw(screen)
        pygame.time.wait(70)

    def spawn_Ennemy(self, Ennemy_class_name):
        ennemy = Ennemy_class_name(self)
        self.all_ennemy.add(ennemy)

    def check_collition(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
