import pygame
from pathlib import PurePath
from Objects.ColorPalette import ColorPalette
from Objects.Sprite import Sprite


class Bird:
    def __init__(self, y_coord, x_coord=60):
        """
        Initializes a new bird object
        :param y_coord: The position of the bird on the x-axis
        :param x_coord: The position of the bird on the y-axis
        """
        self.__x_coordinate = x_coord
        self.__y_coordinate = y_coord

        # We need the height and width of the canvas for error handling purposes
        self.__canvas_width, self.canvas_height = pygame.display.get_surface().get_size()

        self.__bird_width = 50

        # These limits will ensure that the entirety of the bird is always visible
        self.__upper_limit = self.__bird_width
        self.__lower_limit = self.canvas_height - self.__bird_width

        # The sprite that represents the bird in-game
        self.__sprite = Sprite(str(PurePath("Images/bird_wing_down.png")))
        self.__colorPalette = ColorPalette()

        self.__jumped = False

        self.__pull = -18  # application will result into negative velocity
        self.__gravity = 1  # the force the pulls the bird downward
        self.__velocity = 0  # dictates the speed and direction of the bird

    @property
    def y_coordinate(self):
        return self.__y_coordinate

    @property
    def x_coordinate(self):
        return self.__x_coordinate

    def to_canvas(self, canvas: pygame.Surface):
        """
        Draws the bird onto the specified canvas or surface
        :param canvas: The surface wherein the bird is to be drawn on
        """
        if self.__jumped:
            self.__fly()
        else:
            self.__fall()

        self.__update_position()

        # Parameters for the bird's sprite
        bird_location = (self.x_coordinate, self.y_coordinate)
        bird_dimensions = (self.__bird_width, self.__bird_width)

        # Draw the bird
        self.__sprite.draw(canvas=canvas, location=bird_location, dimensions=bird_dimensions)

    def __fall(self):
        """
        Pushes the bird downward
        """
        if self.__y_coordinate < self.__lower_limit:
            self.__velocity += self.__gravity

    def __fly(self):
        """
        Pushes the bird upward
        :return:
        """
        if self.__y_coordinate > self.__upper_limit:
            self.__velocity += self.__pull

        self.__jumped = False

    def __update_position(self):
        """
        Updates the position of the bird and also restricts it to within the visible area of the canvas
        :return:
        """
        # applies a push or pull force to the bird
        self.__y_coordinate += self.__velocity

        # enforce the limits so the bird will always be visible.
        # velocity is set to zero so the bird won't get 'stuck' when it hits the upper and lower boundaries of
        # the canvas.
        if self.__y_coordinate < 1:
            self.__y_coordinate = self.__upper_limit
            self.__velocity = 0
        elif self.__y_coordinate > self.canvas_height:
            self.__y_coordinate = self.__lower_limit
            self.__velocity = 0

    def jump(self):
        """
        Activate the bird object's flight mechanism
        :return:
        """
        self.__jumped = True
