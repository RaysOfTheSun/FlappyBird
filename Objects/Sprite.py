import pygame


class Sprite(pygame.sprite.Sprite):
    """
    Represents a 2D image in the game
    """
    def __init__(self, image_file):
        """
        Initializes a new instance of the Sprite class \n
        :param image_file: The path to the image that will visually represent the sprite
        """
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.__image = pygame.image.load(image_file).convert_alpha()  # Make blitting easier

    def draw(self, canvas, location, sprite_dimensions=None):
        """
        Draws the image onto the specified canvas or surface \n
        :param canvas: The surface wherein the bird is to be drawn on
        :param location: The x and y coordinates of the area where the image is to be drawn on
        :param sprite_dimensions: The desired width and height of the image
        """
        # Scale the image so that it is the same dimensions as the in-game object
        if sprite_dimensions is not None:
            self.__image = pygame.transform.scale(self.__image, sprite_dimensions).convert_alpha()

        rect = self.__image.get_rect()
        rect.left, rect.top = location

        # Draw the image onto the specified canvas
        canvas.blit(self.__image, rect)
