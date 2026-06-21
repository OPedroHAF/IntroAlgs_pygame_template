import pygame
import config

class TimeManager():
    def __init__(self, fps):
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.dt = 0.0
        self.paused = False

    def toggle_pause(self):
        self.paused = not self.paused
    
    def update(self):
        real_dt = self.clock.tick(self.fps) / 1000.0

        if self.paused == True:
            self.dt = 0.0

        else:
            self.dt = real_dt
            
        return self.dt
        
   
