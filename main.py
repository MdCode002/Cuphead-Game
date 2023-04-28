import pygame
from game import Game
from Arme import Projectile
# from animation import Animation
from Player import Player_ImgLoader
import pygame.mixer
import time


pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

pygame.display.set_caption("Ceuphéde")
screen = pygame.display.set_mode((1024, 576))
floor = pygame.image.load("./assets/Background/part1.png")
background = pygame.image.load("./assets/Background/lv2-2_bg_sky.png")
plat1 = pygame.image.load("./assets/Background/part2plat1.png")
background = pygame.transform.scale(background, (1024, 576))
plat1 = pygame.transform.scale(plat1, (80, 40))


player_idle, player_idleLeft, player_idleRight, Shoot, ShootLeft, run, runRev, current_frame, current_frame_Shoot, current_frame_run, Jump, JumpRev, current_frame_Jump, current_frame_runShoot, RunShoot, hit, frame_imag_hit = Player_ImgLoader()

# Telecharge les image de l'ecran de titre
background_Title = pygame.image.load(
    "./assets/Title/title_screen_background.png")
background_Title = pygame.transform.scale(background_Title, (1024, 576))
imgtitile = []
for i in range(1, 35):
    if i < 10:
        imagesT = pygame.image.load(
            f"./assets/Title/cuphead_title_screen_000{i}.png")
        imagesT = pygame.transform.scale(imagesT, (700, 450))
        imgtitile.append(imagesT)
    else:
        imagesT = pygame.image.load(
            f"./assets/Title/cuphead_title_screen_00{i}.png")
        imagesT = pygame.transform.scale(imagesT, (700, 450))

        imgtitile.append(imagesT)

frame_imag_title = 0

hit = False

# text ecran de titre
mapolice = pygame.font.SysFont("Fink Heavy", 50)
text = mapolice.render("Appuyer sur une touche", True, (231, 188, 76))


# initialise la fonction principale
game = Game()
running = True
game.fpsTitle = 0
# projectile = Projectile(g
# pour utiliser les touche du claviere
keys = pygame.key.get_pressed()

# Joue le son en boucle indéfiniment
if not game.is_Playing:
    game.son.play(loops=-1)
JumpX2 = 0
clock = pygame.time.Clock()


def Animation(screen, Tab, rect, current_frame):
    screen.blit(Tab[current_frame], rect)
    current_frame = (current_frame + 1) % len(Tab)


while (running):

    # verifie si le jeu a commencer ou non
    if game.is_Playing:
        # on applique le background et les plztform
        screen.blit(background, (0, 0))
        screen.blit(floor, (0, 250))
        screen.blit(plat1, (400, 280))

        # On lance le jeu
      # game.Player.update_health_bar(screen)
        screen.blit(game.Player.pvimg, game.Player.pvrect)

        # Pour Courire vers la droite
        if game.pressed.get(pygame.K_RIGHT) and not game.pressed.get(pygame.K_LEFT):
            if game.Player.is_jumping == False and not game.pressed.get(pygame.K_z):
                screen.blit(run[current_frame_run], game.Player.rect)
                current_frame_run = (current_frame_run + 1) % len(run)
            player_idle = player_idleRight
            if game.pressed.get(pygame.K_z) and game.Player.is_jumping == False:
                screen.blit(RunShoot[current_frame_runShoot], game.Player.rect)
                current_frame_runShoot = (
                    current_frame_runShoot + 1) % len(RunShoot)
            if game.Player.rect.x < 880:
                game.Player.moveRight()

            # Pour Courire vers la Gauche
        if game.pressed.get(pygame.K_LEFT) and not game.pressed.get(pygame.K_RIGHT):
            if game.Player.is_jumping == False:
                screen.blit(runRev[current_frame_run], game.Player.rect)
                current_frame_run = (current_frame_run + 1) % len(runRev)
            player_idle = player_idleLeft
            if game.Player.rect.x > 60:
                game.Player.moveLeft()
        #  Appliquer le dégat a la colistion
        if game.check_collition(game.Player, game.all_ennemy):
            if game.Player.health > 0:
                if time.monotonic() - game.Player.time_last_colistion > 3:
                    game.Player.health -= 1
                    game.Player.pvimg = game.Player.pvimgs[game.Player.health]
                    game.Player.rect.x = game.Player.rect.x - 100
                    hit = True
                    game.Player.time_last_colistion = time.monotonic()
                    if game.Player.health == 0:
                        game.game_over()

         # Animation fit du joueru hit, frame_imag_hit
        # if hit:

        # On definit si le projectile vas ver la droite ou vers la gauche

        for projectile in game.Player.all_Projectiles:
            if projectile.direction == "none":
                if player_idle == player_idleRight:

                    projectile.move()
                else:
                    projectile.moveLeft()
            elif projectile.direction == "Right":
                projectile.move()
            elif projectile.direction == "Left":
                projectile.moveLeft()

        # Lancer Projectile et Animation Idle du player
        if game.pressed.get(pygame.K_z) and game.Player.is_jumping == False:
            # Lancer le projectile
            game.Player.Lancer_Projectile()
            # idle vers la gauche
            if player_idle == player_idleLeft and not game.pressed.get(pygame.K_RIGHT) and not game.pressed.get(pygame.K_LEFT):
                tmp = pygame.transform.flip(
                    Shoot[current_frame_Shoot], True, False)
                screen.blit(tmp, game.Player.rect)
                current_frame_Shoot = (current_frame_Shoot + 1) % len(Shoot)
            # idle vers la droite
            else:
                if not game.pressed.get(pygame.K_RIGHT) and not game.pressed.get(pygame.K_LEFT):
                    screen.blit(Shoot[current_frame_Shoot], game.Player.rect)
                    current_frame_Shoot = (
                        current_frame_Shoot + 1) % len(Shoot)
            # recuperer les projectile du joueur

        elif ((not game.pressed.get(pygame.K_RIGHT) and not game.pressed.get(pygame.K_LEFT)) or (game.pressed.get(pygame.K_RIGHT) and game.pressed.get(pygame.K_LEFT))) and game.Player.is_jumping == False:
            game.Player.image = player_idle[current_frame]
            screen.blit(game.Player.image, game.Player.rect)
            current_frame = (current_frame + 1) % len(player_idle)

        for monster in game.all_ennemy:
            monster.forward()
            monster.animateEnimie(game)
            # monster.update_health_bar(screen)
        if game.pressed.get(pygame.K_RIGHT) and game.pressed.get(pygame.K_LEFT) and game.pressed.get(pygame.K_z):
            if player_idle == player_idleLeft:
                tmp = pygame.transform.flip(
                    Shoot[current_frame_Shoot], True, False)
                screen.blit(tmp, game.Player.rect)
                current_frame_Shoot = (current_frame_Shoot + 1) % len(Shoot)
            else:
                screen.blit(Shoot[current_frame_Shoot], game.Player.rect)
                current_frame_Shoot = (
                    current_frame_Shoot + 1) % len(Shoot)
        # Sauter
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:

        game.Player.all_Projectiles.draw(screen)

        # appliquer l'ensemble des image de mon groupe d'enemy
        game.all_ennemy.draw(screen)

        if game.Player.is_jumping == True:
            if (game.pressed.get(pygame.K_RIGHT) and not game.pressed.get(pygame.K_LEFT)) or player_idle == player_idleRight:
                screen.blit(Jump[current_frame_Jump], game.Player.rect)
                current_frame_Jump = (current_frame_Jump + 1) % len(Jump)
                game.Player.PlayerJump()
            elif game.pressed.get(pygame.K_LEFT) and not game.pressed.get(pygame.K_RIGHT) or player_idle == player_idleLeft:
                screen.blit(JumpRev[current_frame_Jump], game.Player.rect)
                current_frame_Jump = (current_frame_Jump + 1) % len(JumpRev)
                game.Player.PlayerJump()

        pygame.time.wait(40)
        game.son.stop()
    else:
        # if pygame.key.get_pressed():
        #     #
        dt = clock.tick(60)/1000
        game.fpsTitle += dt
        if game.fpsTitle > 0.05:
            screen.blit(background_Title, (0, 0))
            screen.blit(imgtitile[frame_imag_title], (200, 130))
            frame_imag_title = (frame_imag_title + 1) % len(imgtitile)
            screen.blit(text, (350, 500))
            game.fpsTitle -= 0.05

    # mettre a jour l'ecran
    pygame.display.flip()

    for events in pygame.event.get():
        if (events.type == pygame.QUIT):
            running = False
            pygame.quit()
        elif (events.type == pygame.KEYDOWN):
            if not game.is_Playing:
                game.game_start()
            game.pressed[events.key] = True

            if events.key == pygame.K_SPACE:
                game.Player.is_jumping = True

        elif (events.type == pygame.KEYUP):
            game.pressed[events.key] = False
    # clock.tick(60)
