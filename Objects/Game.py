import pygame
from Objects.Bird import Bird
from Objects.PipeSet import PipeSet
from Objects.ColorPalette import ColorPalette
from Sprites.Background import Background

class Game:
    def __init__(self):
        """
        Initializes a new instance of the Game class
        """
        self.colorPalette = ColorPalette()
        self.frame_number = 0

        pygame.init()
        self.screen_size = (600, 800)
        self.canvas = pygame.display.set_mode(self.screen_size, 0, 32)
        pygame.display.set_caption("Flappy Bird")
        self.background = Background("Images/background.png", [0, 0])

        self.bird = Bird(self.screen_size[1] // 2)
        self.pipes = [PipeSet()]
        self.current_pipe = self.pipes[0]

    def clean_canvas(self):
        """
        Removes everything that is drawn on the canvas or surface
        """
        self.canvas.fill(self.colorPalette.black)
        # Draw the background over the canvas
        self.canvas.blit(self.background.image, self.background.rect)

    def play(self):
        """
        Run the game code
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
                elif (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
                    self.bird.jump()

            self.make_pipes()
            for pipe_set in self.pipes:
                pipe_set.to_canvas(self.canvas)
                pipe_set.scroll()

            # as these pipes are no longer visible anyway,
            # remove the PipeSet (pipe) object from the PipeSet collection so it won't grow too much
            if self.current_pipe.x_coordinate < 0:
                self.pipes.pop(0)
                self.current_pipe = self.pipes[0]

            if self.current_pipe.collide(self.bird):
                print("Collision")
                # play_game = False

            self.bird.to_canvas(self.canvas)

            # Update the canvas
            pygame.display.flip()

            # erase everything in the canvas before redrawing so new stuff won't overlap with old stuff
            self.clean_canvas()

        pygame.quit()

    def make_pipes(self):
        """
        Creates a new PipeSet object that will serve as an obstacle in the game
        """
        # Create a new pipe every 60th frame
        if self.frame_number % 60 == 0:
            self.pipes.append(PipeSet())
            self.frame_number = 0  # The frame counter is reset to prevent it from becoming too large

