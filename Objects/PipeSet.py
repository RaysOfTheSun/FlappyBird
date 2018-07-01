import pygame
import random
import math
from pathlib import PurePath
from Objects.ColorPalette import ColorPalette
from Objects.Sprite import Sprite


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
        self.offset = self.pipe_width // 2 # Divide the pipe's width then floor (//) the result

        # Sprites
        self.__pipe_head = Sprite(str(PurePath("res/Images/pipe_head.png")))
        self.__pipe_body = Sprite(str(PurePath("res/Images/pipe_body.png")))

        self.top_pipe_height = 0
        self.bottom_pipe_height = 0
        self.scroll_speed = 2  # How fast the pipes will move towards the bird

        self.calculate_dimensions()

    def to_canvas(self, canvas):
        """
        Draws the bird onto the specified canvas or surface \n
        :param canvas: The surface wherein the bird is to be drawn on
        """
        # top pipe
        # pygame.draw.line(canvas, self.color_palette.white, (self.x_coordinate, 0),
        #                 (self.x_coordinate, self.top_pipe_height), self.pipe_width)
        # bottom pipe
        # pygame.draw.line(canvas, self.color_palette.white, (self.x_coordinate, self.bottom_pipe_height),
        #              (self.x_coordinate, self.canvas_height*2), self.pipe_width)

        # The pipes have the same dimensions for the head sprite
        pipe_head_dimensions = (self.pipe_width, self.offset)

        # Parameters for the top pipe
        top_pipe_body_location = ((self.x_coordinate - self.offset), -self.offset)
        top_pipe_head_location = ((self.x_coordinate - self.offset), (self.top_pipe_height - self.offset))
        top_pipe_body_dimensions = (self.pipe_width, self.top_pipe_height)

        # Parameters for the bottom pipe
        bottom_pipe_body_location = ((self.x_coordinate - self.offset), self.bottom_pipe_height)
        bottom_pipe_head_location = ((self.x_coordinate - self.offset), (self.bottom_pipe_height - self.offset))
        bottom_pipe_body_dimensions = (self.pipe_width, self.bottom_pipe_height*2)

        # Draw the top pipe
        self.__pipe_body.to_canvas(canvas=canvas, location=top_pipe_body_location,
                                   dimensions=top_pipe_body_dimensions)
        self.__pipe_head.to_canvas(canvas=canvas, location=top_pipe_head_location,
                                   dimensions=pipe_head_dimensions)

        # Draw the bottom pipe
        self.__pipe_body.to_canvas(canvas=canvas, location=bottom_pipe_body_location,
                                   dimensions=bottom_pipe_body_dimensions)
        self.__pipe_head.to_canvas(canvas=canvas, location=bottom_pipe_head_location,
                                   dimensions=pipe_head_dimensions)

    def calculate_dimensions(self):
        """
        Calculates the height and gap between the two pipes in the pipe set
        """
        max_height = (self.canvas_height // 2) - self.passable_space_height
        self.top_pipe_height = random.choice(range(self.passable_space_height, max_height))
        self.bottom_pipe_height = random.choice(range(max_height, self.canvas_height))

    def scroll(self):
        """
        Gradually move the pipe towards the bird and off the screen
        """
        self.x_coordinate -= self.scroll_speed

    def collide(self, bird):
        """
        Determines whether the bird had collided with either of the two pipes in the pipe set \n
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

    def is_cleared(self, bird):
        """
        Determines whether the bird has successfully passed through the pipe \n
        :return: True if the bird did not hit any of the pipes in the pipe set
        """
        mid_point_x = (self.x_coordinate + bird.x_coordinate) // 2
        mid_point_y = (self.top_pipe_height + self.bottom_pipe_height) // 2

        # if the bird passes through the are in-between the two pipes, it has cleared the obstacle
        if (bird.x_coordinate == mid_point_x and bird.y_coordinate >= mid_point_y)\
                or (bird.x_coordinate == mid_point_x and bird.y_coordinate <= mid_point_y):
            return True
        else:
            return False
