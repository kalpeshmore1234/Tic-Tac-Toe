from player import RandomComputerPlayer, HumanPlayer, GeniusComputerPlayer
import time
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #(When you are not interested in some values returned by a function we use underscore in place of variable name . Basically it means you are not interested in how many times the loop is run till now just that it should run some specific number of times overall.)
        #we will use a single list to 3*3 board
        self.current_winner = None #keep track of winner

    def print_board(self):

        #This is just getting the rows
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number corresponds to what box)
        number_board = [[str(i) for i in range(j*3 , (j+1)*3)] for j in range(3)]
        for row in number_board:
             print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        
        return [i for i,spot in enumerate(self.board) if spot == ' ']

        """ moves = []
        for (i,spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
            return moves """

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move then make the move (assign square to letter)
        #then return true. if invalid, return false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True 
        return False

    def winner(self, square, letter):
        # winner if 3 in row anywhere... we have to check all of these
        #first let's check the row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([spot == letter for spot in  row]):
            return True

        #check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in  column]):
            return True
         
        #chech diagonals
        #but only if the square is an even number [0,2,4,6,8]
        #these are the only moves possible to win a diagonal
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]] #left to right diagonal
            if all([spot == letter for spot in  diagonal1]):
               return True

            diagonal2 = [self.board[i] for i in [2,4,4]] #right to left diagonal
            if all([spot == letter for spot in  diagonal1]):
               return True

        return False #if all of these fail
        


                
def play(game, x_player, o_player, print_game = True):
    # return the winner of the game!(the letter) or None for a tie
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    #(we don't have to worry about winner because we'll just return that
    #which breaks the loop)
    while game.empty_squares():
    # get the move from the appropriate player
       if letter == 'O':
          square = o_player.get_move(game)
       else:
          square = x_player.get_move(game)

       #let's define a function to actually make a move!
       if game.make_move(square, letter):
           if print_game:
                print(letter + f' makes a move to {square}')
                game.print_board()
                print('') # just the empty line

           if game.current_winner:
              if print_game:
                 print(letter + ' wins!')
              return letter

           

           # after we made our move we need to alternate letters
           letter = 'O' if letter == 'X' else 'X' #switches player
           """ if letter == 'X':
               letter = 'O'
           else:
               letter = 'X' """

    time.sleep(.8)

    print('It\'s a tie')   




if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()

    play(t, x_player, o_player, print_game=True)
