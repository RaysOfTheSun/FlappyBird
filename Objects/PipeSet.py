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
        self.canvas_height, self.canvas_width = pygame.display.get_surface().get_size()
        self.color_palette = ColorPalette()

        self.x_coordinate = self.canvas_height
        self.passable_space_height = 30
        self.pipe_width = 60

        self.top_pipe_height = 0
        self.bottom_pipe_height = 0
        self.scroll_speed = 2

        self.calculate_dimensions()

    def to_canvas(self, canvas):
        """
        Draws the bird onto the specified canvas or surface
        :param canvas: The surface wherein the bird is to be drawn on
        """
        # top pipe
        pygame.draw.line(canvas, self.color_palette.white, (self.x_coordinate, 0),
                         (self.x_coordinate, self.top_pipe_height), self.pipe_width)
        # bottom pipe
        pygame.draw.line(canvas, self.color_palette.white, (self.x_coordinate, self.bottom_pipe_height),
                         (self.x_coordinate, self.canvas_height), self.pipe_width)

    def calculate_dimensions(self):
        """
        Calculates the height and gap between the two pipes in the pipe set
        """
        max_height = (self.canvas_height // 2) - self.passable_space_height
        self.top_pipe_height = random.choice(range(self.passable_space_height, max_height))
        self.bottom_pipe_height = random.choice(range(max_height, self.canvas_height))

    def scroll(self):
        """
        Gradually move the pipe off the screen
        """
        self.x_coordinate -= self.scroll_speed
