import pygame
import random
import math
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
        self.scroll_speed = 3

        self.calculate_dimensions()

    def to_canvas(self, canvas):
        """
        Draws the bird onto the specified canvas or surface
        :param canvas: The surface wherein the bird is to be drawn on
        """
        print(self.x_coordinate)

        # top pipe
        pygame.draw.line(canvas, self.color_palette.white, (self.x_coordinate, 0),
                         (self.x_coordinate, self.top_pipe_height), self.pipe_width)
        # bottom pipe
        pygame.draw.line(canvas, self.color_palette.white, (self.x_coordinate, self.bottom_pipe_height),
                         (self.x_coordinate, self.canvas_height*2), self.pipe_width)

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

    def collide(self, bird):
        """
        Determines whether the bird had collided with either of the two pipes in the pipe set
        :param bird: The bird object that the player controls \n
        :return:True if the bird had collided with any of the pipes in the set
        """
        bird_inside_pipe_area = (bird.x_coordinate >= self.x_coordinate) \
                                and (bird.x_coordinate <= self.x_coordinate + self.pipe_width)
        bird_in_contact = (bird.y_coordinate <= self.top_pipe_height) \
                          or (bird.y_coordinate >= self.bottom_pipe_height)

        if bird_in_contact and bird_inside_pipe_area:
            return True
        else:
            return False
