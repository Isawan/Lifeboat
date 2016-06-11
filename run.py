import numpy as np
import battleship as btl
import string

def main():
    while True:
        newgameinput = input('New game? (Y/N) \nOr generate map? (G)\n')
        if 'y' in newgameinput.lower():
            game = create_new_game()
            print("New game created")
            run(game)
        elif 'n' in newgameinput.lower():
            game = setup_current_game()
            print("Game setup")
            run(game)
        elif 'g' in newgameinput.lower():
            board = new_board()
            for jj in range(board.shape[0]):
                for ii in range(board.shape[1]):
                    if round(board[jj,ii]) == 2:
                        board[jj,ii] = 0
            print(board)

        if 'y' not in input('Play again?'):
            break

    print("Thank you for playing")

            

def run(game):
    board = game['board']
    shiplens = game['ships']
    while True:
        combo = btl.combo_grid(board,shiplens)
        hitcoords = btl.wrandom(combo,10)
        print('Board:\n' + str(board))
        print('Ships:\n' + str(shiplens))
        print('Combo:\n' + str(combo))
        print('Possible positions:\n' + str(hitcoords))
        action = input('What do you want to do?\ns - Set flag\nr - remove ship')
        if 's' in action:
            bombresult = [i for i in input('Enter bomb result (position result[0/1]):\n').split()]
            bombpos = btl.lettotup(bombresult[0])
            bombtype = int(bombresult[1])
            board = btl.set_bomb(board,bombpos[0],bombpos[1],bombtype)
            board = btl.find_clear(board,shiplens)
        elif 'r' in action:
            shipsize = int(input('How big is the ship?'))
            shiplens.remove(shipsize)




def create_new_game():
    shape = [int(i) for i in input('Board size?').split()]
    shiplens = [int(i) for i in input('Ship lengths?').split()]
    game = {
            'board':np.zeros(shape),
            'ships':shiplens
            }
    return game

def setup_current_game():
    board = []
    while True:
        rowin = input('Next row')
        if 'end' in rowin.lower():
            break
        board.append([int(i) for i in rowin.split()])
    shiplens = [int(i) for i in input('Ship lengths?').split()]
    return {'board':np.array(board), 'ships':shiplens}

def new_board():
    shape = [int(i) for i in input('Board Size?').split()]
    print(shape)
    shiplens = [int(i) for i in input('Ship lengths?').split()]
    return btl.create_new_board(shape,shiplens)

main()
