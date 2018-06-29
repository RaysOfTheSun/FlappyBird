import pygame
from Objects.Bird import Bird
from Objects.PipeSet import PipeSet
from Objects.ColorPalette import ColorPalette


class Game:
    def __init__(self):
        """
        Initializes a new instance of the Game class
        """
        self.colorPalette = ColorPalette()

        pygame.init()
        self.screen_size = (800, 800)
        self.canvas = pygame.display.set_mode(self.screen_size, 0, 32)
        pygame.display.set_caption("Flappy Bird")

        self.bird = Bird(self.screen_size[1] // 2)
        self.pipes = [PipeSet()]

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
            # skipping this would make the thing unplayable lol
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play_game = False
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE) or (event.key == pygame.K_UP):
                        self.bird.jumped = True

            # erase everything in the canvas before redrawing so new stuff won't overlap with old stuff
            self.clean_canvas()

            self.make_pipes()
            for pipe in self.pipes:
                pipe.to_canvas(self.canvas)
                pipe.scroll()

            self.bird.to_canvas(self.canvas)

            # Update the canvas
            pygame.display.flip()

        pygame.quit()

    def make_pipes(self):
        frame_count = pygame.time.get_ticks()
        if frame_count % 50 == 0:
            self.pipes.append(PipeSet())
