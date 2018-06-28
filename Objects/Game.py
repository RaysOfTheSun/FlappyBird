import pygame
from Objects.Bird import Bird
from Objects.Pipe import Pipe
from Objects.ColorPalette import ColorPalette


class Game:
    def __init__(self):
        """
        Initializes a new instance of the Game class
        """
        self.colorPalette = ColorPalette()

        pygame.init()
        self.screen_size = (600, 800)
        self.canvas = pygame.display.set_mode(self.screen_size, 0, 32)
        pygame.display.set_caption("Flappy Bird")

        self.bird = Bird(self.screen_size[1] // 2)

    def clean_canvas(self):
        """
        Removes everything that is drawn on the canvas or surface
        :return:
        """
        self.canvas.fill(self.colorPalette.black)

    def play(self):
        """
        Runs the game code
        :return:
        """
        clock = pygame.time.Clock()
        play_game = True
        while play_game:
            # Set the frame rate to 60 frames per second (FPS)
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play_game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jumped = True

            # erase everything in the canvas before redrawing so stuff won't overlap
            self.clean_canvas()
            self.bird.draw(self.canvas)

            # Update the canvas
            pygame.display.flip()

        pygame.quit()
