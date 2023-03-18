import MemoryGame
import GuessGame
import CurrencyRouletteGame

games = {
    1: MemoryGame.play,
    2: GuessGame.play,
    3: CurrencyRouletteGame.play,
}


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WOG).\nHere you can find many cool games to play.")


def load_game():
    game_number_message = "Please choose a game number from 1 to 3: "
    game_difficulty_message = "Please choose game difficulty from 1 to 5: "
    print('''Our games:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    ''')

    game_number = input(game_number_message)

    while True:
        if type(game_number) == int or game_number.isdigit():
            game_number = int(game_number)
            if game_number < 1 or game_number > 3:
                game_number = input("Please choose a game number from 1 to 3: ")
            else:
                game_difficulty = input(game_difficulty_message)
                if game_difficulty.isdigit():
                    game_difficulty = int(game_difficulty)
                    if game_number < 1 or game_difficulty > 5:
                        game_difficulty_message = "Game difficulty must be from 1 to 5: "
                    else:
                        break
                else:
                    game_difficulty_message = "Game difficulty must be a number from 1 to 5: "
        else:
            game_number_message = "Game number must be a number from 1 to 3: "
            game_number = input(game_number_message)

    if games[game_number](game_difficulty):
        print('You win!')
    else:
        print('You lose!')
