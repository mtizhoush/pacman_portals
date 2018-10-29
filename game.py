import pygame
import pygame.gfxdraw
from maze import Maze
from eventloop import EventLoop
from pacman import Pacman

class Game:
    BLACK = (0,0,0)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 670))
        pygame.display.set_caption("Pacman Portal")

        self.radius = 1
        self.start = 1
        self.end = 10
        self.begin = pygame.time.get_ticks()
        self.wait = 800

        self.maze = Maze(self.screen, mazefile='images/maze.txt', brickfile='square',
                         portalfile='portal', shieldfile='shield', pointfile='powerpill')

    def __str__(self): return 'Game(Pacman Portal)' + str(self.maze) + ')'

    def open_portal(self, x, y, color):
        for r in range(self.start, self.end):
            pygame.gfxdraw.circle(self.screen, x, y, r, color)
        now = pygame.time.get_ticks()
        if (now < self.begin + self.wait): self.inc = 1
        elif (now <self.begin + 4 * self.wait): self.inc = 0
        else: self.inc = -1
        self.start += self.inc
        self.start = max(1, self.start)
        self.end += self.inc

    def play(self):
        eloop = EventLoop(finished=False)

        while not eloop.finished:
            eloop.check_events()
            self.update_screen()

    def update_screen(self):
        self.screen.fill(Game.BLACK)
        self.maze.blitme()
        self.open_portal(100, 100, (240, 100, 20))
        #self.open_portal(100, 100, (0, 0, 240))
        pygame.display.flip()

game = Game()
game.play()