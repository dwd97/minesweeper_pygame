import sys
import pygame
import configuration as config
import game_logic as logic
import drawing_logic as interface
import saving_system as save_sys


def main():
    global screen
    
    """
    screen - used for displaying
    clock - used for settings FPS
    
    """
    pygame.init()
    screen = config.set_pygame_config()
    clock = pygame.time.Clock()
    game = logic.MinesweeperGame()
    game.start_time = pygame.time.get_ticks()
    interface_object = interface.Interface()
    last_recorded_time = 0
    
    running = True
    
    state_menu = True
    state_game = False

    while running:
        clock.tick(config.FPS)
        screen.fill(config.COLOR_FRAME)
        
        if state_menu:
            play_btn, selection_btns = interface_object.draw_the_ui_menu(screen)
        elif state_game:
            mines_left_in_the_board = game.mines_left_in_the_board()
            interface_object.draw_the_board(game.board, screen)
            time = 0
            if(game.is_running and not game.end_of_game):
                time = (pygame.time.get_ticks() - game.start_time) // 1000
                last_recorded_time = time
                restart_btn, menu_btn = interface_object.draw_the_ui_panel(time, mines_left_in_the_board, screen)
            elif(not game.is_running and not game.end_of_game):
                restart_btn, menu_btn = interface_object.draw_the_ui_panel(time, mines_left_in_the_board, screen)
            else:
                restart_btn, menu_btn = interface_object.draw_the_ui_panel(last_recorded_time, mines_left_in_the_board, screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                if(state_game):
                    if(mouse_x < config.BOARD_WIDTH):
                        column = mouse_x // config.SIZE_OF_SQUARE
                        row = mouse_y // config.SIZE_OF_SQUARE
                        
                        if(event.button == 1):
                            game.reveal_square(row, column)
                        elif(event.button == 3):
                            game.toggle_flag(row, column)
                    elif(restart_btn.collidepoint(mouse_x, mouse_y)):
                        if(event.button == 1):
                            game.new_game()
                    elif(menu_btn.collidepoint(mouse_x, mouse_y)):
                        if(event.button == 1):
                            config.revert_default_UI_config()
                            screen = config.set_pygame_config()
                            state_game = False
                            state_menu = True
                if(state_menu):
                    if(play_btn.collidepoint(mouse_x, mouse_y)):
                        if(event.button == 1):
                            game.new_game()
                            screen = config.set_pygame_config()
                            state_menu = False
                            state_game = True
                    for i in range(len(selection_btns)):
                        if(selection_btns[i].collidepoint(mouse_x, mouse_y)):
                            if(event.button == 1):
                                save_sys.SELECTED_DIFFICULTY = i + 1
        
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()