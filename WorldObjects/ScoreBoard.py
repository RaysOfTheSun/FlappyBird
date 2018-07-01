import pygame
from pathlib import PurePath
from Objects.ColorPalette import ColorPalette


class ScoreBoard:
    def __init__(self):
        self.__font = pygame.font.Font(str(PurePath("res/Fonts/04B_19.TTF")), 70)
        self.__color_palette = ColorPalette()
        self.sound = pygame.mixer.Sound(str(PurePath("res/sounds/sfx_point.wav")))

    def to_canvas(self, canvas, score):
        """
        Draws the scoreboard onto the specified canvas or surface \n
        :param canvas: The surface wherein the bird is to be drawn on
        :param score: The numbers to be drawn onto the specified surface or canvas
        :return:
        """
        score_surface = self.__font.render(score, False, self.__color_palette.white_smoke)
        score_surface_shadow = self.__font.render(score, False, self.__color_palette.black)
        canvas.blit(score_surface_shadow, (305, 50))
        canvas.blit(score_surface, (300, 50))

    def buzz(self):
        """
        Plays a sound
        """
        self.sound.play()
