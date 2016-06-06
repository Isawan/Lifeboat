import string
import numpy as np
import matplotlib.pyplot as plt

def lettotup(pos):
    let = dict(zip(string.ascii_lowercase,[ord(c)%32 for c in string.ascii_lowercase]))
    return (int(pos[0])-1,let[pos[1]]-1)

# TODO: Test
def test_ship(board,ship):
    def is_out_of_bounds():
        def outbounds(x,y,sx,sy):
            return x < 0 or y < 0 or x => sx or y =>y
        return (outbounds(ship[0],ship[1],board.shape[0],board.shape[1]) or
                outbounds(ship[0] + ship[2]-1, ship[1] + ship[3] -1,
                    board.shape[0],board.shape[1]))
    def is_legal():
        for jj in xrange(ship[1], ship[3]):
            for ii in xrange(ship[0], ship[2]):
                if board[jj][ii] == 'x' or  board [jj][ii] == 'n':
                    return false
    return not ( is_out_of_bounds() && is_legal() )
