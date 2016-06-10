import random as r
import string
import numpy as np
import matplotlib.pyplot as plt

WTR = 0
SHP = 1
CLR = 2

bombable = set([WTR])

def lettotup(pos):
    let = dict(zip(string.ascii_lowercase,[ord(c)%32 for c in string.ascii_lowercase]))
    return (int(pos[0])-1,let[pos[1]]-1)

def valid_placement(board,ship):
    def is_out_of_bounds():
        def outbounds(x,y,sx,sy):
            return x < 0 or y < 0 or x >= sx or y >= sy
        return (outbounds(ship[0],ship[1],board.shape[1],board.shape[0]) or
                outbounds(ship[0] + ship[2]-1, ship[1] + ship[3] -1,
                    board.shape[1],board.shape[0]))
    def is_legal():
        for jj in range(ship[1], ship[1] + ship[3]):
            for ii in range(ship[0], ship[0] + ship[2]):
                if board[jj][ii] == CLR:
                    return False
        return True
    return ( not is_out_of_bounds() ) and is_legal()

def ship_combinations(x,y,shiplength):
    ships = []
    for ii in range(shiplength):
        #horizontal
        ships.append((x-ii,y,shiplength,1))
        #vertical
        ships.append((x,y-ii,1,shiplength))
    return set(ships)

def valid_combinations(board,x,y,shiplength):
    combo = []
    for ship in ship_combinations(x,y,shiplength):
        if valid_placement(board,ship):
            combo.append(ship)
    return set(combo)

def combo_grid(board,shiplengths):
    combogrid = np.zeros(board.shape)
    for jj in range(board.shape[0]):
        for ii in range(board.shape[1]):
            for ss in shiplengths:
                combogrid[jj][ii] += len(valid_combinations(board,ii,jj,ss))
    return combogrid

def set_ship(board,ship):
    board = np.copy(board)
    def setclr(x,y):
        def outbounds(x,y):
            return x < 0 or y < 0 or x >= board.shape[1] or y >= board.shape[0]
        for jj in range(y-1,y+2):
            for ii in range(x-1,x+2):
                if (not outbounds(ii,jj)) and board[jj,ii] == WTR:
                    board[jj,ii] = CLR
        return board

    for jj in range(ship[1],ship[1] + ship[3]):
        for ii in range(ship[0], ship[0] + ship[2]):
            if board[jj,ii] == SHP:
                return (board,False)
    for jj in range(ship[1],ship[1] + ship[3]):
        for ii in range(ship[0], ship[0] + ship[2]):
            board[jj, ii] = SHP
    for jj in range(ship[1],ship[1] + ship[3]):
        for ii in range(ship[0], ship[0] + ship[2]):
             board = setclr(ii,jj)
    return (board,True)

def create_new_board(shape,shiplengths):
    board = np.zeros(shape)
    for sl in sorted(shiplengths,reverse=True):
        while True:
            com = valid_combinations(board,r.randrange(shape[1]), r.randrange(shape[0]),sl)
            if not com:
                continue
            board,success = set_ship(board,r.choice(list(com)))
            if not success:
                continue
            break
    return board

def set_bomb(board,x,y,r):
    board = np.copy(board)
    def outbounds(x,y):
       return x < 0 or y < 0 or x >= board.shape[1] or y >= board.shape[0]
    if r == WTR:
        board[y,x] = CLR
    if r == SHP:
        board[y,x] = SHP
    for jj in range(board.shape[0]):
        for ii in range(board.shape[1]):
            if board[jj,ii] == SHP:
                for kk in (ii+1,ii-1):
                    for ll in (jj+1,jj-1):
                        if not outbounds(kk,ll) and board[kk,ll] == WTR:
                            board[kk,ll] = CLR
    return board

