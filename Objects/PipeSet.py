import pygame
import random
from Objects.ColorPalette import ColorPalette


class PipeSet:
    """
    Represents an obstacle in the game
    """
    def __init__(self):
        """
        Initializes a new instance of the pipe class
        """
        self.x_coordinate = 800
        self.y_coordinate = 0
        self.width = 60

        self.top = 0
        self.bottom = 0

        self.scroll_speed = 3
        self.offset = 16

        self.color_palette = ColorPalette()

        self.calculate_dimensions(pygame.display.get_surface().get_size())

    def to_canvas(self, canvas):
        """
        Draws the bird onto the specified canvas or surface
        :param canvas: The surface wherein the bird is to be drawn on
        :return:
        """
        # top pipe
        pygame.draw.line(canvas, self.color_palette.white, (self.x_coordinate, self.y_coordinate),
                         (self.x_coordinate, self.y_coordinate + self.top), self.width)
        # bottom pipe
        pygame.draw.line(canvas, self.color_palette.white, (self.x_coordinate, self.y_coordinate + self.bottom),
                         (self.x_coordinate, 800), self.width)

    def calculate_dimensions(self, canvas_dimensions):
        """
        Calculates the height and gap between the two pipes in the pipe set
        :param canvas_dimensions: The height and width of the canvas where the pipe set is to be drawn onto
        :return:
        """
        canvas_height, canvas_width = canvas_dimensions
        limit = (canvas_height // 2) + self.offset

        self.top = random.choice(range(0, limit))
        self.bottom = random.choice(range(limit, canvas_height))

    def scroll(self):
        """
        Gradually move the pipe off-screen
        :return:
        """
        self.x_coordinate -= self.scroll_speed
