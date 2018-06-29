import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        """
        Initializes a new instance of the background class
        :param image_file: The path to the image that would serve as the background
        :param location: The relative path to the location of the image to be used
        """
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location