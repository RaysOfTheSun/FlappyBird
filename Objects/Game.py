import pygame
from Objects.Menu import Menu
from Objects.Bird import Bird
from Objects.PipeSet import PipeSet
from WorldObjects.Ground import Ground
from WorldObjects.Backdrop import Backdrop
from WorldObjects.ScoreBoard import ScoreBoard
from Objects.ColorPalette import ColorPalette


class Game:
    def __init__(self):
        """
        Initializes a new instance of the Game class
        """
        self.colorPalette = ColorPalette()
        self.frame_number = 0

        # initialization of Pygame components
        pygame.init()
        self.screen_size = (600, 800)  # width x height
        self.canvas = pygame.display.set_mode(self.screen_size, 0, 32)
        pygame.display.set_caption("Flappy Bird")

        # Initialization of game models
        self.ground = Ground(self.screen_size)
        self.background = Backdrop(self.ground.offset)
        self.bird = Bird(ground_offset=self.ground.offset, y_coord=self.screen_size[1] // 2)
        self.pipes = [PipeSet()]
        self.menu_pipes = [PipeSet()]

        self.menu = Menu(canvas_dimensions=self.screen_size)

        self.player_points = 0
        self.scoreboard = ScoreBoard()

    def clean_canvas(self):
        """
        Removes everything that is drawn on the canvas or surface
        """
        self.canvas.fill(self.colorPalette.black)
        self.background.to_canvas(canvas=self.canvas)

    def play(self):
        """
        Run the game code
        """
        clock = pygame.time.Clock()
        play_game = False
        just_launched = True

        while not play_game and just_launched:
            clock.tick(60)
            self.frame_number += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    just_launched = False
                elif (event.type == pygame.KEYDOWN) or (event.type == pygame.MOUSEBUTTONDOWN):
                    # reset the frame counter as not doing so would mess up pipe generation
                    # once the actual game starts
                    self.frame_number = 0
                    play_game = True

            self.background.to_canvas(canvas=self.canvas)

            self.make_pipes(self.menu_pipes)
            for pipe_set in self.menu_pipes:
                pipe_set.to_canvas(canvas=self.canvas)
                pipe_set.scroll()

            self.ground.to_canvas(canvas=self.canvas)

            self.menu.to_canvas(canvas=self.canvas)

            pygame.display.flip()

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

            self.make_pipes(self.pipes)
            for pipe_set in self.pipes:
                pipe_set.to_canvas(canvas=self.canvas)
                pipe_set.scroll()

            # In case the current pipe goes off-screen (i.e. its position in the x-axis becomes negative)
            # remove the PipeSet (pipe) object from the PipeSet collection so it won't grow too much
            if self.pipes[0].x_coordinate <= 0:  # Pipe width
                self.pipes.pop(0)

            # Only check if the bird will collide with the pipe that is in front of it
            if self.pipes[0].collide(bird=self.bird):
                self.bird.hit_sound.play()
                # play_game = False
            elif self.pipes[0].is_cleared(bird=self.bird):
                self.player_points += 1
                self.scoreboard.buzz()

            self.bird.to_canvas(canvas=self.canvas)

            self.ground.to_canvas(canvas=self.canvas)

            self.scoreboard.to_canvas(canvas=self.canvas, score=str(self.player_points))

            # Update the canvas so what we've drawn will be seen
            pygame.display.flip()

            # erase everything in the canvas before redrawing so new stuff won't overlap with old stuff
            self.clean_canvas()

            print(f"FPS: {clock.get_fps()}")

        pygame.quit()

    def make_pipes(self, pipe_set):
        """
        Creates a new PipeSet object that will serve as an obstacle in the game
        """
        # Every 60 frames, we draw a new pipe
        if self.frame_number % 60 == 0:
            pipe_set.append(PipeSet())
            self.frame_number = 0  # The frame counter is reset to prevent it from becoming too large

