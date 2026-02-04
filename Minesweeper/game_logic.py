import random
import configuration as config
import saving_system as save_sys
import pygame

class GameSquare:
    """GameSquare and its variables"""
    def __init__(self):
        self.mine = False
        self.flag = False
        self.number = 0
        self.revealed = False
        
class MinesweeperGame:
    """
    Defines the class for the Minesweeper game instance to save game state and check for different game occurencess such as winning state, lose state
    """
    def __init__(self):
        self.board = []
        self.start_time = 0
        self.end_of_game = False
        self.has_won = False
        self.is_running = False
        self.start_pos = None
    
    def new_game(self):
        """
        Starts a new game
        Mines are placed only after the first click is registered
        """
        difficulty = save_sys.SELECTED_DIFFICULTY
        config.NUMBER_OF_COLUMNS = config.DIFFICULTIES[difficulty][0]
        config.NUMBER_OF_ROWS = config.DIFFICULTIES[difficulty][1]
        config.NUMBER_OF_MINES = config.DIFFICULTIES[difficulty][2]
        
        config.calculate_UI_config()
        
        self.board = [[GameSquare() for _ in range(config.NUMBER_OF_COLUMNS)] for _ in range(config.NUMBER_OF_ROWS)]
        self.end_of_game = False
        self.has_won = False
        self.start_pos = None
        self.is_running = False
    
    def generate_mines_on_the_board(self, board):
        """
        It generates mines randomly on the board
        """
        coordinates = []
        
        def start_pos_further_than_two_from_bomb(start_position, bomb_position):
            if(abs(start_position[0] - bomb_position[0]) < 2 and abs(start_position[1] - bomb_position[1]) < 2):
                return False
            else:
                return True
        
        while len(coordinates) < config.NUMBER_OF_MINES:
            column = random.randint(0,config.NUMBER_OF_COLUMNS-1)
            row = random.randint(0,config.NUMBER_OF_ROWS-1)
            if([column,row] not in coordinates):
                if(start_pos_further_than_two_from_bomb(self.start_pos, [column, row])):
                    coordinates.append([column,row])
        
        for i in range(0, len(coordinates)):
            column = coordinates[i][0]
            row = coordinates[i][1]
            board[row][column].mine = True
    
        return board
    
    def generate_numbers_on_the_board(self, board):
        """
        It generates the numbers that indicate how close a mine is to a game square.
        """
        for row in range(config.NUMBER_OF_ROWS):
            for column in range(config.NUMBER_OF_COLUMNS):
                number = 0
                directions = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
                for direction in directions:
                    if(row + direction[1] >= 0 and column + direction[0] >= 0 and row + direction[1] < config.NUMBER_OF_ROWS and column + direction[0] < config.NUMBER_OF_COLUMNS):
                        if(board[row + direction[1]][column + direction[0]].mine is True):
                            number += 1
                board[row][column].number = number
        return board
    
    def reveal_square(self, row, column):
        """
        The user will reveal a square with the left click. In main loop.
        """
        if(self.end_of_game) or not (0 <= row < config.NUMBER_OF_ROWS) or not (0 <= column < config.NUMBER_OF_COLUMNS):
            return
        
        if(self.start_pos == None):
            self.start_pos = [column, row]
            self.board = self.generate_mines_on_the_board(self.board)
            self.board = self.generate_numbers_on_the_board(self.board)
            self.is_running = True
            self.start_time = pygame.time.get_ticks()
        
        game_square = self.board[row][column]
        if(game_square.revealed or game_square.flag):
            return
        
        game_square.revealed = True
        
        if(game_square.mine):
            self.end_of_game = True
            self.has_won = False
            self.reveal_all_mines()
        else:
            if(game_square.number == 0):
                self.reveal_blank_game_squares(row, column)
            self.check_has_won()
    
    def toggle_flag(self, row, column):
        """The right mouse button click toggles the flag on the game_square."""
        if(self.end_of_game) or not (0 <= row < config.NUMBER_OF_ROWS) or not (0 <= column < config.NUMBER_OF_COLUMNS):
            return
        
        game_square = self.board[row][column]
        if(not game_square.revealed):
            game_square.flag = not game_square.flag
    
    def reveal_blank_game_squares(self, row, column):
        """
        It reveals blank game squares after the user clicks on a game square to reveal.
        """
        directions = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
        
        # a queue with only one element, the starting one to reveal the other ones
        stack = [[self.board[row][column], row, column]]
        
        while stack != []:
            game_square = stack.pop()
            
            for direction in directions:
                new_row = game_square[1] + direction[1]
                new_column = game_square[2] + direction[0]
                if(new_row >= 0 and new_column >= 0 and new_row < config.NUMBER_OF_ROWS and new_column < config.NUMBER_OF_COLUMNS):
                    if(self.board[new_row][new_column].revealed == False and self.board[game_square[1]][game_square[2]].number == 0):
                        self.board[new_row][new_column].revealed = True
                        stack.append([self.board[new_row][new_column], new_row, new_column])
    
    def reveal_all_mines(self):
        """
        After a square with a mine is revealed, all other squares with mines are also revealed.
        """
        for row in range(config.NUMBER_OF_ROWS):
            for column in range(config.NUMBER_OF_COLUMNS):
                if(self.board[row][column].mine):
                    self.board[row][column].revealed = True
    
    def check_has_won(self):
        """
        After every revealed game square, this function checks whether the user has won.
        """
        revealed_without_mine = 0
        
        for row in range(config.NUMBER_OF_ROWS):
            for column in range(config.NUMBER_OF_COLUMNS):
                if(not self.board[row][column].mine and self.board[row][column].revealed):
                    revealed_without_mine += 1
        
        game_squares_total = config.NUMBER_OF_COLUMNS * config.NUMBER_OF_ROWS
        
        if(revealed_without_mine == (game_squares_total - config.NUMBER_OF_MINES)):
            self.has_won = True
            self.end_of_game = True
            save_sys.save_successful_game((pygame.time.get_ticks() - self.start_time)//1000)
            
    def mines_left_in_the_board(self):
        """
        It returns how many mines are left in the board that the user has not found. It calculates the amount using flags.
        """
        if(self.board == []):
            return
        
        number_of_flags = 0
        
        for row in range(config.NUMBER_OF_ROWS):
            for column in range(config.NUMBER_OF_COLUMNS):
                if(self.board[row][column].flag):
                    number_of_flags += 1
        
        return config.NUMBER_OF_MINES - number_of_flags