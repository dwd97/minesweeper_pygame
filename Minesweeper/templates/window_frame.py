import sys
sys.path.append("..")

import pygame
import configuration as config

class UI_Frame:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.width = width
        self.height = height
        self.shadow_width = 0
        self.frame_width = 0
        self.draw()
    
    def draw(self):
        frame_width = 25
        self.frame_width = frame_width
        
        top_rectangle = pygame.Rect(self.x+0, self.y+0, self.width, frame_width)
        bottom_rectangle = pygame.Rect(self.x+0,self.y+self.height - frame_width ,self.width, frame_width)
        left_rectangle = pygame.Rect(self.x+0,self.y+0,frame_width, self.height)
        right_rectangle = pygame.Rect(self.x+self.width - frame_width, self.y+0, frame_width, self.height)
        
        pygame.draw.rect(self.screen, config.COLOR_FRAME, top_rectangle)
        pygame.draw.rect(self.screen, config.COLOR_FRAME, bottom_rectangle)
        pygame.draw.rect(self.screen, config.COLOR_FRAME, left_rectangle)
        pygame.draw.rect(self.screen, config.COLOR_FRAME, right_rectangle)
        
        shadow_width = 4
        self.shadow_width = shadow_width
        
        #outer shadow
        #ten bily nahore
        pygame.draw.polygon(self.screen, config.COLOR_WHITE, ([self.x+0,self.y+0], [self.x+shadow_width,self.y+shadow_width], [self.x+self.width - shadow_width, self.y+shadow_width], [self.x+self.width, self.y+0]), 0)
        #ten bily vlevo
        pygame.draw.polygon(self.screen, config.COLOR_WHITE, ([self.x+0,self.y+0], [self.x+shadow_width,self.y+shadow_width], [self.x+shadow_width, self.y+self.height - shadow_width], [self.x+0, self.y+self.height]),0)
        # ten sedy dole
        pygame.draw.polygon(self.screen, config.COLOR_LIGHT_GRAY, ([self.x+0, self.y+self.height], [self.x+shadow_width, self.y+self.height - shadow_width], [self.x+self.width-shadow_width, self.y+self.height-shadow_width], [self.x+self.width, self.y+self.height]),0)
        # ten sedy vpravo
        pygame.draw.polygon(self.screen, config.COLOR_LIGHT_GRAY, ([self.x+self.width, self.y+self.height], [self.x+self.width - shadow_width, self.y+self.height - shadow_width], [self.x+self.width - shadow_width, self.y+shadow_width], [self.x+self.width, self.y+0]),0)
        
        #inner shadow
        # levy svetle sedy
        pygame.draw.polygon(self.screen, config.COLOR_LIGHT_GRAY, ([self.x+frame_width - shadow_width, self.y+frame_width - shadow_width], [self.x+frame_width - shadow_width, self.y+self.height + shadow_width - frame_width], [self.x+frame_width, self.y+self.height - frame_width], [self.x+frame_width, self.y+frame_width]),0)
        # svetle sedy nahore
        pygame.draw.polygon(self.screen, config.COLOR_LIGHT_GRAY, ([self.x+frame_width - shadow_width, self.y+frame_width - shadow_width], [self.x+frame_width, self.y+frame_width], [self.x+self.width - frame_width, self.y+frame_width], [self.x+self.width - frame_width + shadow_width, self.y+frame_width - shadow_width]), 0)
        # bily vpravo
        pygame.draw.polygon(self.screen, config.COLOR_WHITE, ([self.x+self.width - frame_width + shadow_width, self.y+frame_width - shadow_width], [self.x+self.width - frame_width, self.y+frame_width], [self.x+self.width - frame_width, self.y+self.height - frame_width], [self.x+self.width - frame_width + shadow_width, self.y+self.height - frame_width + shadow_width]), 0)
        # bily dole
        pygame.draw.polygon(self.screen, config.COLOR_WHITE, ([self.x+self.width - frame_width, self.y+self.height - frame_width], [self.x+self.width - frame_width + shadow_width, self.y+self.height - frame_width + shadow_width], [self.x+frame_width - shadow_width, self.y+self.height - frame_width + shadow_width], [self.x+frame_width, self.y+self.height - frame_width]), 0)
    
    def get_frame_rect(self):
        return pygame.Rect(self.x + self.frame_width, self.y + self.frame_width, self.width - self.frame_width * 2, self.height - self.frame_width * 2)