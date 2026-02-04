import pygame
import configuration as config
import templates.window_frame as frame
import templates.button as btn
import templates.digital_number_display as digiNum
import saving_system as save_sys
import templates.selection_buttons as select_btns

class Interface:
    def __init__(self):
        return
    
    def draw_the_board(self, board, screen):
        """Draws the board, without mines."""
        if(board == []):
            return
    
        for r in range(config.NUMBER_OF_ROWS):
            for s in range(config.NUMBER_OF_COLUMNS):
                x = s * config.SIZE_OF_SQUARE
                y = r * config.SIZE_OF_SQUARE
                board_square = board[r][s]
                square_button = (x,y,config.SIZE_OF_SQUARE, config.SIZE_OF_SQUARE)

                if board_square.revealed:
                    pygame.draw.rect(screen, config.COLOR_OPEN_SQUARE, square_button)
                    if board_square.mine:
                        pygame.draw.rect(screen, config.COLOR_RED, square_button)
                        # ta cerna bomba
                        pygame.draw.circle(screen, config.COLOR_BLACK, (x+20,y+20), 10)
                        # to ostny bomby
                        pygame.draw.line(screen, config.COLOR_BLACK, (x+5, y+20), (x+35,y+20), 4)
                        pygame.draw.line(screen, config.COLOR_BLACK, (x+20, y+5), (x+20,y+35), 4)
                        # to bile kolecko
                        pygame.draw.circle(screen, config.COLOR_WHITE, (x+18, y+18), 3)
                        # dalsi stripky z bomby
                        pygame.draw.circle(screen, config.COLOR_BLACK, (x+30,y+30), 2)
                        pygame.draw.circle(screen, config.COLOR_BLACK, (x+10,y+10), 2)
                        pygame.draw.circle(screen, config.COLOR_BLACK, (x+30,y+10), 2)
                        pygame.draw.circle(screen, config.COLOR_BLACK, (x+10,y+30), 2)
                    elif board_square.number > 0:
                        colors_of_numbers = {0: config.COLOR_1, 1: config.COLOR_1, 2: config.COLOR_2, 3: config.COLOR_3, 4: config.COLOR_4, 5: config.COLOR_5, 6: config.COLOR_6, 7: config.COLOR_7, 8: config.COLOR_8}
                        color_of_the_number = colors_of_numbers[board_square.number]
                        
                        text = config.FONT_CONFIG.render(str(board_square.number), True, color_of_the_number)
                        screen.blit(text, (x+14,y+10))
                else:
                    #to zakryte board_square
                    pygame.draw.rect(screen, config.COLOR_CLOSED_SQUARE, square_button)
                    #ten polygon v policku nahore
                    pygame.draw.polygon(screen, config.COLOR_WHITE, [(x,y), (x+40, y),(x+35,y+5), (x+5, y+5)], 0)
                    #ten polygon v policku vlevo
                    pygame.draw.polygon(screen, config.COLOR_WHITE, [(x,y), (x, y+40),(x+5,y+35), (x+5, y+5)], 0)
                    #ten polygon v policku dole
                    pygame.draw.polygon(screen, config.COLOR_LIGHT_GRAY, [(x,y+40), (x+40, y+40),(x+35, y+35),(x+5,y+35)], 0)
                    #ten polygon v policku vpravo
                    pygame.draw.polygon(screen, config.COLOR_LIGHT_GRAY, [(x+40,y+40), (x+40, y),(x+35, y+5),(x+35,y+35)], 0)
                    if(board_square.flag):
                        # ta vlajkova cast vlajky
                        pygame.draw.polygon(screen, config.COLOR_RED, [(x+20,y+20), (x+20, y+10), (x+10, y+15)])
                        # ten stozar vlajky
                        pygame.draw.line(screen, config.COLOR_BLACK, (x+20,y+10), (x+20, y+25),  2)
                        # ta podstava pro vlajku
                        pygame.draw.polygon(screen, config.COLOR_BLACK, [(x+10, y+30), (x+30, y+30), (x+20, y+25)],0)

                pygame.draw.rect(screen, config.COLOR_BLACK, square_button, 1)
        
    def draw_the_ui_panel(self, time, mines_left_in_the_board, screen):
        """
        It draws the UI panel on the left
        """
        
        this_frame = frame.UI_Frame(config.BOARD_WIDTH, 0, config.UI_WIDTH, config.BOARD_HEIGHT, screen)
        frame_rect = this_frame.get_frame_rect()
        
        digiNum_height_time = 50
        digiNum.UI_Text(time, frame_rect.x, frame_rect.y, frame_rect.width, digiNum_height_time, screen)
        
        digiNum_height_mine = 50
        digiNum.UI_Text(mines_left_in_the_board, frame_rect.x, frame_rect.y + digiNum_height_time, frame_rect.width, digiNum_height_mine, screen)
        
        btn_height_menu = 70
        btn_height_restart = 70
        
        menu_btn = btn.UI_Button("Menu", frame_rect.x, frame_rect.y + frame_rect.height - btn_height_menu - btn_height_restart, frame_rect.width, btn_height_menu, screen)
        restart_btn = btn.UI_Button("Restart", frame_rect.x, frame_rect.y + frame_rect.height - btn_height_restart, frame_rect.width, btn_height_restart, screen)
        
        return restart_btn.get_rect(), menu_btn.get_rect()
        
    def draw_the_ui_menu(self, screen):
        """
        It draws the menu with the frame and the buttons. In the game state or when triggered by the programmer.
        """
        
        pygame.draw.rect(screen, config.COLOR_BACKGROUND, pygame.Rect(config.WINDOW_WIDTH, config.BOARD_HEIGHT, 0, 0))
        
        
        
        this_frame = frame.UI_Frame(0,0,config.WINDOW_WIDTH, config.BOARD_HEIGHT, screen)
        frame_rect = this_frame.get_frame_rect()
        
        best_time = save_sys.get_best_time()
        
        if(best_time != None):
            text = config.FONT_CONFIG.render(f"Best time: {best_time} seconds", True, config.COLOR_WHITE)
            text_rect = text.get_rect(center=(frame_rect.width/2 + 10, frame_rect.y + 50))
            screen.blit(text, text_rect)
        else:
            text = config.FONT_CONFIG.render(f"Your best time will appear here", True, config.COLOR_WHITE)
            text_rect = text.get_rect(center=(frame_rect.width/2 + 10, frame_rect.y + 50))
            screen.blit(text, text_rect)
        
        btn_height = 70
        btn_width = 200
        btn_x = ((frame_rect.x + frame_rect.width) // 2) - (btn_width // 2)
        
        play_btn = btn.UI_Button("Play", btn_x, frame_rect.y + frame_rect.height // 3, btn_width, btn_height, screen)
        
        difficulty_selection_buttons = select_btns.UI_Button(config.DIFFICULTIES, frame_rect.x, frame_rect.y + frame_rect.height - btn_height, frame_rect.width, btn_height, screen)
        
        return play_btn.get_rect(), difficulty_selection_buttons.get_rect()