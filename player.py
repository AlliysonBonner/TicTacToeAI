import random


class Player:
    """Represents a player in the game.

    Attributes:
        letter (str): A string representing the player's letter ('X' or 'O').

    Methods:
        get_move(game): Get the player's next move given the current game state.
    """

    def __init__(self, letter):
        """Initializes a new instance of the Player class.

        Args:
            letter (str): A string representing the player's letter ('X' or 'O').
        """
        self.letter = letter

    def get_move(self, game):
        """Get the player's next move given the current game state.

        This method must be implemented by all subclasses of the Player class.

        Args:
            game (TicTacToe): The current TicTacToe game instance.

        Returns:
            int: The index of the square the player has chosen to mark on the board.
        """
        pass


class SmartComputerPlayer(Player):
    """Represents a computer player that uses the minimax algorithm to make smart moves.

    Inherits from the Player class.

    Attributes:
        letter (str): A string representing the player's letter ('X' or 'O').

    Methods:
        get_move(game): Get the computer player's next move given the current game state.
    """

    def __init__(self, letter):
        """Initializes a new instance of the SmartComputerPlayer class.

        Args:
            letter (str): A string representing the player's letter ('X' or 'O').
        """
        super().__init__(letter)

    def get_move(self, game):
        """Get the computer player's next move given the current game state.

        Uses the minimax algorithm to choose the best move.

        Args:
            game (TicTacToe): The current TicTacToe game instance.

        Returns:
            int: The index of the square that the computer player has chosen to mark on the board.
        """
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) # choose a random corner
        else:
            # get the best move using the minimax algorithm
            _, square = self.minimax(game, self.letter)

        return square

    def minimax(self, game, player):
        """Recursive function that evaluates all possible moves and returns the best move for the player.

        Args:
            game (TicTacToe): The current TicTacToe game instance.
            player (str): A string representing the current player ('X' or 'O').

        Returns:
            tuple: A tuple containing the best score and the index of the best move.
        """
        other_player = 'O' if player == 'X' else 'X'

        # base cases
        if game.current_winner == self.letter:
            return 1, None
        elif game.current_winner == other_player:
            return -1, None
        elif not game.empty_squares():
            return 0, None

        # recursive case
        if player == self.letter:
            # maximize the score
            best_score = float('-inf')
            best_move = None
            for move in game.available_moves():
                game.make_move(move, player)
                score, _ = self.minimax(game, other_player)
                game.board[move] = ' '
                game.current_winner = None
                if score > best_score:
                    best_score = score
                    best_move = move
        else:
            # minimize the score
            best_score = float('inf')
            best_move = None
            for move in game.available_moves():
                game.make_move(move, player)
                score, _ = self.minimax(game, self.letter)
                game.board[move] = ' '
                game.current_winner = None
                if score < best_score:
                    best_score = score
                    best_move = move

        return best_score, best_move



class HumanPlayer(Player):
    """Represents a human player that gets moves from user input.

    Inherits from the Player class.

    Attributes:
        letter (str): A string representing the player's letter ('X' or 'O').

    Methods:
        get_move(game): Get the human player's next move given the current game state.
    """

    def __init__(self, letter):
        """Initializes a new instance of the HumanPlayer class.

        Args:
            letter (str): A string representing the player's letter ('X' or 'O').
        """
        super().__init__(letter)

    def get_move(self, game):
        """Get the human player's next move given the current game state.

        Prompts the user to input a square to mark on the board, validates the input,
        and returns the index of the chosen square.

        Args:
            game (TicTacToe): The current TicTacToe game instance.

        Returns:
            int: The index of the square the user has chosen to mark on the board.
        """
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")
        return val
