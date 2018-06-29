import pygame


class Bird(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        """
        Initializes a new instance of the bird class
        :param image_file: The path to the image that would serve as the background
        :param location: The relative path to the location of the image to be used
        """
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image = pygame.image.load(image_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

