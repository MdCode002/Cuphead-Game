# import pygame

# # class pour les animation


# class AnimateSprite(pygame.sprite.Sprite):
#     # definire les chose a faire a ala creation de l'entité
#     def __init__(self, sprite_name):
#         super().__init__()
#         self.image = pygame.image.load(f"./assets/Ennemy/lv3-2_satyr_skip_0001.png")
#         self.curent_image = 0
#         self.images = animation.get(sprite_name)

#     # definir une methode pour anime le sprite
#     def animate(self):

#         # passer a l'image suivante
#         self.curent_image += 1

#         # verifier si on a attenit la fin de l'animation
#         if self.curent_image > len(self.images): 
#             self.curent_image = 0

#         # changer d'image
#         self.image = self.images[self.curent_image]


# # definir une fonction pour charger les image d'un sprite
# def load_animation_images(self,sprite_name):
#     # charger  les image
#     images = []
#     # trcuperer le chemin du dossier
#     path = f"assetes/{sprite_name}"

#     # boucle sur chaque image dans ce dossier
#     for i in range(1, 10):
#         image_path = path + str(i) + 'png'
#         images.append(pygame.image.load(image_path))

#     return images


# # definir un dectionnaire qui va contenur les image
# animation = {
#     'Ennemy': load_animation_images('Ennemy/lv3-2_satyr_skip_000'),
# }

def Animation(screen,Tab,rect,current_frame):
     screen.blit(Tab[current_frame], rect)
     current_frame = (current_frame + 1) % len(Tab)