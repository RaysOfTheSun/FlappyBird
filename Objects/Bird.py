import pygame
from Objects.ColorPalette import ColorPalette

class Bird:
    def __init__(self, y_coord, x_coord=64):
        """
        Initializes a new bird object
        :param y_coord: The position of the bird on the x-axis
        :param x_coord: The position of the bird on the y-axis
        """
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord

        self.colorPalette = ColorPalette()

        # We need the height and width of the canvas for error handling purposes
        self.canvas_width, self.canvas_height = pygame.display.get_surface().get_size()

        self.jumped = False
        self.downward_force = 1
        self.upward_force = 0

    def draw(self, canvas: pygame.Surface):
        """
        Draws the bird onto the specified canvas or surface
        :param canvas: The surface wherein the bird is to be drawn on
        :return:
        """
        if self.jumped:
            print("FLAP")
        else:
            self.fall()

        pygame.draw.circle(canvas, self.colorPalette.white, (self.x_coordinate, self.y_coordinate), 16, 16)

    def fall(self):
        """
        Pushes the bird downward
        :return:
        """
        if self.y_coordinate < self.canvas_height:
            self.upward_force += self.downward_force
            self.y_coordinate += self.upward_force
