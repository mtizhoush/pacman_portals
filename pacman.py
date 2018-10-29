import pygame
from pygame.sprite import Sprite
from timer import Timer
from vector import Vector

class Pacman(Sprite):
    def __init__(self, screen, maze, posn, direction):
        super().__init__(screen, maze, posn, direction)

        self.sz = 30
        self.frames = []
        self.diedframes = []
        self.wait = 25
        self.frame_index = 0
        self.dead = False

        self.frames = self.loadimage('pacman', Pacman.NUM_FRAMES)
        self.frames_dying = self.loadimages('pacman_die', Pacman.NUM_FRAMES_DIED)

        self.timer = Timer(frames=self.frames, wait=self.wait)
        self.timerdead = Timer(frames=self.frames_dying, wait=self.wait)

        self.rect = pygame.Rect(posn.x, posn.y, self.sz, self.sz)
        self.playing = False
        #self.pacman_eating
        #self.pacman_dying
        #self.pacman_super

    def __str__(self):
        return 'Pacman(direction=' + str(self.direction) + ', posn=' + str(self.posn) +\
               ', dead=?' + str(self.dead) + ')'

    def update(self):
        super().update()
        self.rect.x = self.posn.x
        self.rect.y = self.posn.y
        if(self.moving and not self.playing):
            self.playing = True

        elif not self.moving and self.playing:
            self.playing = False

        #update position
        #decide if it ate a ghost

    def change_direction(self, direction):
        self.direction = direction

    def blitme(self):
        imgrect = self.timer.imagerect() if not self.dead else self.timerdead.imagerect
        angle = Pacman.rotations(self.direction)
        img = pygame.transform.rotate(imgrect.image, angle)
        self.screen.blit(img, self.rect)
