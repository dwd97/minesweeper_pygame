import sys
sys.path.append("..")

import pygame
import configuration as config

class UI_Text:
    def __init__(self, number, x, y, width, height, screen):
        self.number = number
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.draw()
    
    def draw(self):
        
        margin = 4
        
        rectangle = pygame.Rect(self.x + margin, self.y + margin, self.width - margin * 2, self.height - margin * 2)
        pygame.draw.rect(self.screen, config.COLOR_BLACK, rectangle)
        
        self.draw_digits(self.number, self.x + margin, self.y + margin, self.width - margin*2, self.height-margin*2)
    
    def draw_digits(self, number, x, y, width, height):
        digit_list = [] # first is the Least significant digit
        
        if (number == 0):
            digit_list = [0]
        else:
            while number > 0:
                digit_list.append(number % 10)
                number = number // 10
        
        number_width = width//6
        number_height = height - 8
        number_y = y + 4
        number_offset = 5
        
        numbers_mapping = {1: 0b00110000, 2: 0b01101110, 3: 0b01111010, 4: 0b00110011, 5: 0b01011011, 6: 0b01011111, 7: 0b01110000, 8: 0b01111111, 9: 0b01111011, 0: 0b01111101}
        
        for i in range(len(digit_list)):
            self.draw_one_digit(numbers_mapping[digit_list[i]], x+width - (number_width + number_offset) * (i + 1) , number_y ,number_width,number_height)
                    
    
    # Number will be in 0b01234567 (7-digit), see programmer's documentation for more information
    def draw_one_digit(self, bit_sequence,x,y,width,height):
        col_1 = config.COLOR_RED if (bit_sequence & 0x40) != 0 else config.COLOR_DARK_GRAY
        col_2 = config.COLOR_RED if (bit_sequence & 0x20) != 0 else config.COLOR_DARK_GRAY
        col_3 = config.COLOR_RED if (bit_sequence & 0x10) != 0 else config.COLOR_DARK_GRAY
        col_4 = config.COLOR_RED if (bit_sequence & 0x08) != 0 else config.COLOR_DARK_GRAY
        col_5 = config.COLOR_RED if (bit_sequence & 0x04) != 0 else config.COLOR_DARK_GRAY
        col_6 = config.COLOR_RED if (bit_sequence & 0x02) != 0 else config.COLOR_DARK_GRAY
        col_7 = config.COLOR_RED if (bit_sequence & 0x01) != 0 else config.COLOR_DARK_GRAY
        
        thickness = 4
        offset = 2
        digit_width = width
        digit_height = height // 2
        #1
        pygame.draw.polygon(self.screen, col_1, ([x, y], [x + digit_width, y], [x + digit_width - thickness, y + thickness], [x + thickness, y + thickness]),0)
        
        #2
        pygame.draw.polygon(self.screen, col_2, ([x+digit_width, y+offset], [x+digit_width-thickness, y+thickness+offset], [x+digit_width-thickness, y+digit_height-thickness-offset], [x+digit_width, y+digit_height-offset]),0)
        
        #3
        pygame.draw.polygon(self.screen, col_3, ([x+digit_width, y+digit_height + offset], [x+digit_width - thickness, y+digit_height+thickness+offset], [x+digit_width-thickness, y+digit_height*2-thickness-offset], [x+digit_width, y+digit_height*2-offset]),0)
        
        #4
        pygame.draw.polygon(self.screen, col_4, ([x, y+digit_height*2], [x+thickness, y+digit_height*2-thickness], [x+digit_width-thickness, y+digit_height*2-thickness], [x+digit_width, y+digit_height*2]),0)
        
        #5
        pygame.draw.polygon(self.screen, col_5, ([x, y+digit_height + offset], [x+thickness, y+digit_height+thickness + offset], [x+thickness, y+digit_height*2-thickness - offset], [x,y+digit_height*2 - offset]))
        
        #6
        pygame.draw.polygon(self.screen, col_6, ([x + offset, y+digit_height], [x+thickness, y+digit_height-thickness//2], [x+digit_width-thickness, y+digit_height-thickness//2], [x+digit_width - offset, y+digit_height], [x+digit_width-thickness, y+digit_height+thickness//2], [x+thickness, y+digit_height+thickness//2]))
        
        #7
        pygame.draw.polygon(self.screen, col_7, ([x,y + offset], [x+thickness, y+thickness + offset], [x+thickness, y+digit_height-thickness - offset], [x, y+digit_height - offset]))