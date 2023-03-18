from Live import load_game, welcome

print(welcome(input('Enter your name: ')))

while True:
    load_game()

    another_game = input('Do you want to play again? (y/n): ')
    if another_game.lower() != 'y':
        print('Thanks for playing!')
        break
