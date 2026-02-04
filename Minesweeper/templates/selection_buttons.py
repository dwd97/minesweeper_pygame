import sys
sys.path.append("..")

import pygame
import configuration as config
import saving_system as save_sys

class UI_Button:
    def __init__(self, options, x, y, width, height, screen):
        self.options = options
        self.x = x
        self.y = y
        self.screen = screen
        self.width = width
        self.height = height
        self.currently_selected = None
        self.draw()
    
    def draw(self):
        shadow_width = 5
        number_of_btns = len(self.options)
        
        for i in range(number_of_btns):
            btn_width = self.width // number_of_btns
            btn_x = self.x + i * btn_width
            rectangle = pygame.Rect(btn_x, self.y, btn_width, self.height)
            color = config.COLOR_SELECTED if save_sys.SELECTED_DIFFICULTY == i + 1 else config.COLOR_FRAME
            pygame.draw.rect(self.screen, color, rectangle)
            
            # centrovany text
            text = config.FONT_CONFIG.render(f"{i+1}", True, config.COLOR_WHITE)
            text_rect = text.get_rect(center=(btn_width/2, self.height/2))
            self.screen.blit(text, (btn_x + text_rect.x, self.y + text_rect.y))
            
            #stiny
            # bily nahore
            pygame.draw.polygon(self.screen, config.COLOR_WHITE, ([btn_x, self.y], [btn_x + shadow_width, self.y + shadow_width], [btn_x + btn_width - shadow_width, self.y + shadow_width], [btn_x + btn_width, self.y]),0)
            # bily vlevo
            pygame.draw.polygon(self.screen, config.COLOR_WHITE, ([btn_x, self.y], [btn_x + shadow_width, self.y + shadow_width], [btn_x + shadow_width, self.y + self.height - shadow_width], [btn_x, self.y + self.height]),0)
            # svetle sedy vpravo
            pygame.draw.polygon(self.screen, config.COLOR_LIGHT_GRAY, ([btn_x + btn_width, self.y], [btn_x + btn_width - shadow_width, self.y + shadow_width], [btn_x + btn_width - shadow_width, self.y + self.height - shadow_width], [btn_x + btn_width, self.y + self.height]),0)
            # svetle sedy dole
            pygame.draw.polygon(self.screen, config.COLOR_LIGHT_GRAY, ([btn_x + btn_width, self.y + self.height], [btn_x + btn_width - shadow_width, self.y + self.height - shadow_width], [btn_x + shadow_width, self.y + self.height - shadow_width], [btn_x, self.y + self.height]))
        
        
        
    def get_rect(self):
        btns = []
        for i in range(len(self.options)):
            btn_width = self.width // len(self.options)
            btn_x = self.x + i * btn_width
            btns.append(pygame.Rect(btn_x, self.y, btn_width, self.height))
        return btns