import pygame
from pathlib import PurePath
from GameModules.ColorPalette import ColorPalette


class GameOverMenu:
    """
    The game over screen
    """
    def __init__(self, canvas_dimensions):
        """
        Initializes a new instance of the GameOverMenu class \n
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
        self.__prompt_font = pygame.font.Font(str(PurePath("res/Fonts/04B_19.TTF")), 30)

        self.game_title_surface = self.__title_font.render("Game", False, self.__color_palette.orange)
        self.game_highlight_surface = self.__highlight_font.render("Game", False, self.__color_palette.white_smoke)

        self.over_title_surface = self.__title_font.render("Over", False, self.__color_palette.orange)
        self.over_highlight_surface = self.__highlight_font.render("Over", False, self.__color_palette.white_smoke)

        self.__title_surface = self.__title_font.render("Score", False, self.__color_palette.salmon)
        self.__background_rect = pygame.Rect(self.canvas_height // 9, self.canvas_width // 2 - 50, 400, 200)
        self.__background_rect_outline = pygame.Rect(self.canvas_height // 10 - 4,
                                                     self.canvas_width // 2 - 60, 425, 220)
        self.score_header_surface = self.__title_font.render("Score:", False, self.__color_palette.orange)
        self.best_header_surface = self.__title_font.render("Best:", False, self.__color_palette.orange)

        # Initialize prompt text
        self.prompt_surface = self.__prompt_font.render("Press anything to play again", False,
                                                        self.__color_palette.dark_golden_rod)
        self.prompt_surface_shadow = self.__prompt_font.render("Press anything to play again", False,
                                                               self.__color_palette.white_smoke)

    def to_canvas(self, canvas, score):
        """
        Draws the screen onto the specified canvas
        :param canvas: The surface wherein the game over menu is to be drawn on
        :param score: The player's final score
        """

        score_text_surface = self.__title_font.render(str(score), False, self.__color_palette.orange)

        canvas.blit(self.game_highlight_surface, ((self.canvas_width // 5) - 5, 150))
        canvas.blit(self.over_highlight_surface, ((self.canvas_width // 2) + 15, 150))

        canvas.blit(self.game_title_surface, ((self.canvas_width // 5), 150))
        canvas.blit(self.over_title_surface, ((self.canvas_width // 2) + 20, 150))

        pygame.draw.rect(canvas, self.__color_palette.dark_golden_rod, self.__background_rect_outline)
        pygame.draw.rect(canvas, self.__color_palette.pale_golden_rod, self.__background_rect)

        canvas.blit(self.score_header_surface, ((self.canvas_width // 5), (self.canvas_height // 2) - 120))
        canvas.blit(self.best_header_surface, ((self.canvas_width // 5), (self.canvas_height // 2) - 50))
        canvas.blit(score_text_surface, ((self.canvas_width // 2) + 30, self.canvas_height // 2 - 120))
        canvas.blit(score_text_surface, ((self.canvas_width // 2) + 30, self.canvas_height // 2 - 50))

        # Draw the prompt text
        canvas.blit(self.prompt_surface_shadow, ((self.canvas_width // 8) - 5, (self.canvas_height // 2) + 100))
        canvas.blit(self.prompt_surface, ((self.canvas_width // 8), (self.canvas_height // 2) + 100))


