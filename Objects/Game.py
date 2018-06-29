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
        self.frame_number = 0

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
            self.frame_number += 1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    play_game = False
                if event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_SPACE) or (event.key == pygame.K_UP):
                        self.bird.jumped = True

            self.make_pipes()
            for pipe_set in self.pipes:
                pipe_set.to_canvas(self.canvas)
                pipe_set.scroll()

                # as these pipes are no longer visible anyway,
                # remove the PipeSet (pipe) object from the array so it won't grow too much
                if pipe_set.x_coordinate < 0:
                    self.pipes.remove(pipe_set)

            self.bird.to_canvas(self.canvas)

            # Update the canvas
            pygame.display.flip()

            # erase everything in the canvas before redrawing so new stuff won't overlap with old stuff
            self.clean_canvas()

        pygame.quit()

    def make_pipes(self):
        # Create a new pipe every 60th frame
        if self.frame_number % 60 == 0:
            self.pipes.append(PipeSet())
            self.frame_number = 0  # The frame counter is reset to prevent it from becoming too large

