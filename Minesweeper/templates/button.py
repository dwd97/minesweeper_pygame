import sys
sys.path.append("..")

import pygame
import configuration as config

class UI_Button:
    def __init__(self, text, x, y, width, height, screen):
        self.text = text
        self.x = x
        self.y = y
        self.screen = screen
        self.width = width
        self.height = height
        self.draw()
    
    def draw(self):
        shadow_width = 5
        
        rectangle = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, config.COLOR_FRAME, rectangle)
        
        # shadows
        # the white one at the top
        pygame.draw.polygon(self.screen, config.COLOR_WHITE, ([self.x, self.y], [self.x + shadow_width, self.y + shadow_width], [self.x + self.width - shadow_width, self.y + shadow_width], [self.x + self.width, self.y]),0)
        # the white one on the left
        pygame.draw.polygon(self.screen, config.COLOR_WHITE, ([self.x, self.y], [self.x + shadow_width, self.y + shadow_width], [self.x + shadow_width, self.y + self.height - shadow_width], [self.x, self.y + self.height]),0)
        # the light gray on the right
        pygame.draw.polygon(self.screen, config.COLOR_LIGHT_GRAY, ([self.x + self.width, self.y], [self.x + self.width - shadow_width, self.y + shadow_width], [self.x + self.width - shadow_width, self.y + self.height - shadow_width], [self.x + self.width, self.y + self.height]),0)
        # light gray bottom
        pygame.draw.polygon(self.screen, config.COLOR_LIGHT_GRAY, ([self.x + self.width, self.y + self.height], [self.x + self.width - shadow_width, self.y + self.height - shadow_width], [self.x + shadow_width, self.y + self.height - shadow_width], [self.x, self.y + self.height]))
        
        
        # centrovany text
        text = config.FONT_CONFIG.render(self.text, True, config.COLOR_WHITE)
        text_rect = text.get_rect(center=(self.width/2, self.height/2))
        self.screen.blit(text, (self.x + text_rect.x, self.y + text_rect.y))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)