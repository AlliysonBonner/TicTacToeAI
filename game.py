from player import HumanPlayer, SmartComputerPlayer
import time


class TicTacToe:
    """
    Class representing the Tic Tac Toe game.

    Attributes:
        board (list): List representing the game board.
        current_winner (str): Current winner of the game.
    """

    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        """
        Prints the game board to the console.
        """
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        """
        Prints the numbered game board to the console.
        """
        number_board = [[str(i) for i in range(j * 3, (j + 1) * 3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        """
        Returns a list of available moves.
        """
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        """
        Checks if there are empty squares left on the board.
        """
        return ' ' in self.board

    def num_empty_squares(self):
        """
        Returns the number of empty squares left on the board.
        """
        return len(self.available_moves())

    def make_move(self, square, letter):
        """
        Makes a move on the board.

        Args:
            square (int): The square to make the move in.
            letter (str): The letter to make the move with.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """
        Checks if the current move made by the given letter leads to a win.

        Args:
            square (int): The square to make the move in.
            letter (str): The letter to make the move with.

        Returns:
            bool: True if the move leads to a win, False otherwise.
        """
        row_ind = square // 3
        row = self.board[row_ind * 3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind + i * 3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    """Plays the Tic Tac Toe game.

    Args:
        game (TicTacToe): The game instance.
        x_player (Player): The player who uses X's.
        o_player (Player): The player who uses O's.
        print_game (bool): Whether to print the game progress.

    Returns:
        str: The winner (either 'X' or 'O') or 'Tie'.

    """
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter

    # iterate while the game still has empty squares
    while game.empty_squares():

        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # make a move and check for a winner
        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')  # add an empty line for readability

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

        # after we made our move, we need to alternate letters
        letter = 'O' if letter == 'X' else 'X'  # switch players

        # add a tiny delay for human vs. computer games
        time.sleep(0.8)

    if print_game:
        print('It\'s a tie')

    return 'Tie'


if __name__ == "__main__":
    while True:
        choice = input("Would you like to be X or O? ").upper()
        if choice == "X":
            human_player = HumanPlayer("X")
            computer_player = SmartComputerPlayer("O")
            break
        elif choice == "O":
            human_player = HumanPlayer("O")
            computer_player = SmartComputerPlayer("X")
            break
        else:
            print("Invalid choice. Please enter 'X' or 'O'.")

    while True:
        mode = input("Would you like to play against a human or the computer? "
                     ).lower()
        if mode == "human":
            play(TicTacToe(), human_player, HumanPlayer("O"))
            break
        elif mode == "computer":
            play(TicTacToe(), human_player, computer_player)
            break
        else:
            print("Invalid mode. Please enter 'human' or 'computer'.")
