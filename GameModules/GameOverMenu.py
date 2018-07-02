import pygame
from pathlib import PurePath
from GameModules.ColorPalette import ColorPalette


class GameOverMenu:
    """
    The game over screen
    """
    def __init__(self, score, canvas_dimensions):
        """
        Initializes a new instance of the GameOverMenu class \n
        :param score: The player's final score
        :param canvas_dimensions: A width x height tuple representing the dimensions of the canvas wherein the
        menu is to be drawn
        """
        self.__color_palette = ColorPalette()
        self.frame_number = 0

        self.canvas_width, self.canvas_height = canvas_dimensions

        # Import resources
        self.__title_font = pygame.font.Font(str(PurePath("res/Fonts/04B_19.TTF")), 65)
        self.__highlight_font = pygame.font.Font(str(PurePath("res/Fonts/04B_19.TTF")), 70)
        self.__outline_font = pygame.font.Font(str(PurePath("res/Fonts/04B_19.TTF")), 75)

        self.__score_font = pygame.font.Font(str(PurePath("res/Fonts/04B_19.TTF")), 30)

        self.game_title_surface = self.__title_font.render("Game", False, self.__color_palette.orange)
        self.game_highlight_surface = self.__highlight_font.render("Game", False, self.__color_palette.white_smoke)

        self.over_title_surface = self.__title_font.render("Over", False, self.__color_palette.orange)
        self.over_highlight_surface = self.__highlight_font.render("Over", False, self.__color_palette.white_smoke)

        self.__title_surface = self.__title_font.render("Score", False, self.__color_palette.salmon)
        self.__background_rect = pygame.Rect(self.canvas_height // 9, self.canvas_width // 2 - 50, 400, 200)
        self.__background_rect_outline = pygame.Rect(self.canvas_height // 10 - 4, self.canvas_width // 2 - 60, 425, 220)

        self.score = score

    def to_canvas(self, canvas):
        """
        Draws the screen onto the specified canvas
        :param canvas: The surface wherein the game over menu is to be drawn on
        """
        canvas.blit(self.game_highlight_surface, ((self.canvas_width // 5) - 5, 150))
        canvas.blit(self.over_highlight_surface, ((self.canvas_width // 2) + 15, 150))

        canvas.blit(self.game_title_surface, ((self.canvas_width // 5), 150))
        canvas.blit(self.over_title_surface, ((self.canvas_width // 2) + 20, 150))

        pygame.draw.rect(canvas, self.__color_palette.dark_golden_rod, self.__background_rect_outline)
        pygame.draw.rect(canvas, self.__color_palette.pale_golden_rod, self.__background_rect)







