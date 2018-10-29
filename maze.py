import pygame
from imagerect import ImageRect


class Maze:
    RED = (255, 0, 0)
    BRICK_SIZE = 13

    def __init__(self, screen, mazefile, brickfile, portalfile, shieldfile, pointfile):
        self.screen = screen
        self.filename = mazefile
        with open(self.filename, 'r') as f:
            self.rows = f.readlines()

        self.bricks = []
        self.shields = []
        self.hportals = []
        self.vportals = []
        self.points = []

        sz = Maze.BRICK_SIZE
        self.brick = ImageRect(screen, brickfile, sz, sz)
        self.shield = ImageRect(screen, shieldfile, sz, sz)
        self.hportal = ImageRect(screen, portalfile, sz, 5 * sz)
        self.vportal = ImageRect(screen, portalfile, sz, 5 * sz)
        self.vportal.image = pygame.transform.rotate(self.vportal.image, 90)
        self.point = ImageRect(screen, pointfile, int(0.5*sz), int(0.5*sz))

        self.deltax = self.deltay = Maze.BRICK_SIZE

        self.build()

    def __str__(self): return 'maze' + self.filename + ')'

    def build(self):
        r = self.brick.rect
        rshield = self.shield.rect
        rhportal = self.hportal.rect
        rvportal = self.vportal.rect
        rpoint = self.point.rect
        w, h = r.width, r.height
        dx, dy, = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'X':
                    self.bricks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'o':
                    self.shields.append(pygame.Rect(ncol * dx, nrow * dy, rshield.width, rshield.height))
                elif col == 'h':
                    self.hportals.append(pygame.Rect(ncol * dx, nrow * dy, rhportal.width, rshield.height))
                elif col == 'v':
                    self.vportals.append(pygame.Rect(ncol * dx, nrow * dy, rvportal.width, rshield.height))
                elif col == 'f':
                    self.points.append(pygame.Rect(ncol * dx, nrow * dy, rpoint.width , rshield.height))

    def blitme(self):
        for rect in self.bricks:
            self.screen.blit(self.brick.image, rect)
        for rect in self.shields:
            self.screen.blit(self.shield.image, rect)
        for rect in self.hportals:
            self.screen.blit(self.hportal.image, rect)
        for rect in self.vportals:
            self.screen.blit(self.vportal.image, rect)
        for rect in self.points:
            self.screen.blit(self.point.image, rect)
