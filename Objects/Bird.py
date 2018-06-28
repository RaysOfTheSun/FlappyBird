import pygame
from Objects.ColorPalette import ColorPalette


class Bird:
    def __init__(self, y_coord, x_coord=60):
        """
        Initializes a new bird object
        :param y_coord: The position of the bird on the x-axis
        :param x_coord: The position of the bird on the y-axis
        """
        self.x_coordinate = x_coord
        self.y_coordinate = y_coord

        # We need the height and width of the canvas for error handling purposes
        self.canvas_width, self.canvas_height = pygame.display.get_surface().get_size()

        self.width = 20

        # These limits will ensure that the entirety of the bird is always visible
        self.upper_limit = self.width
        self.lower_limit = self.canvas_height - self.width

        self.colorPalette = ColorPalette()

        self.jumped = False

        self.pull = -18  # application will result into negative velocity
        self.gravity = 1  # the force the pulls the bird downward
        self.velocity = 0

    def to_canvas(self, canvas: pygame.Surface):
        """
        Draws the bird onto the specified canvas or surface
        :param canvas: The surface wherein the bird is to be drawn on
        :return:
        """
        if self.jumped:
            self.fly()
        else:
            self.fall()

        self.update_position()
        pygame.draw.circle(canvas, self.colorPalette.white, (self.x_coordinate, self.y_coordinate),
                           self.width, self.width)

    def fall(self):
        """
        Pushes the bird downward
        :return:
        """
        if self.y_coordinate < self.lower_limit:
            self.velocity += self.gravity

    def fly(self):
        """
        Pushes the bird upward
        :return:
        """
        if self.y_coordinate > self.upper_limit:
            self.velocity += self.pull

        self.jumped = False

    def update_position(self):
        """
        Updates the position of the bird and also restricts it to within the visible area of the canvas
        :return:
        """
        # applies a push or pull force to the bird
        self.y_coordinate += self.velocity

        # enforce the limits so the bird will always be visible.
        # velocity is set to zero so the bird won't get 'stuck' when it hits the boundaries of the canvas.
        if self.y_coordinate < 1:
            self.y_coordinate = self.upper_limit
            self.velocity = 0
        elif self.y_coordinate > self.canvas_height:
            self.y_coordinate = self.lower_limit
            self.velocity = 0
