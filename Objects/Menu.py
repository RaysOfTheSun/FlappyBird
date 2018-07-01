import pygame
from pathlib import PurePath
from Objects.ColorPalette import ColorPalette


class Menu:
    def __init__(self, canvas_dimensions):
        self.__color_palette = ColorPalette()
        self.frame_number = 0

        self.canvas_width, self.canvas_height = canvas_dimensions
        self.shadow_offset = 8

        # Import resources
        self.__title_font = pygame.font.Font(str(PurePath("res/Fonts/04B_19.TTF")), 70)
        self.__prompt_font = pygame.font.Font(str(PurePath("res/Fonts/04B_19.TTF")), 30)

    def to_canvas(self, canvas):
        """
        Draws the menu to the specified canvas
        """

        title_surface = self.__title_font.render("Flappy Bird", False, self.__color_palette.white_smoke)
        title_surface_shadow = self.__title_font.render("Flappy Bird", False, self.__color_palette.black)

        prompt_surface = self.__prompt_font.render("Press anything to play", False, self.__color_palette.white_smoke)
        prompt_surface_shadow = self.__prompt_font.render("Press anything to play", False, self.__color_palette.black)

        # Draw the title text
        canvas.blit(title_surface_shadow, ((self.canvas_width // 5) + self.shadow_offset, self.canvas_width // 2))
        canvas.blit(title_surface, (self.canvas_width // 5, self.canvas_width // 2))

        # Draw the prompt text
        canvas.blit(prompt_surface_shadow, ((self.canvas_width // 5) + 25, self.canvas_width // 2 + 80))
        canvas.blit(prompt_surface, ((self.canvas_width // 5) + 20, self.canvas_width // 2 + 80))


