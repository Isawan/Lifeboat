import numpy as np
import matplotlib.pyplot as plt
import battleship as btl

from battleship import WTR,SHP,CLR

def test_valid_placement():
    board = np. zeros((10,10))
    expected_ship_result = {
            (0,0,1,1):True,
            (1,0,1,1):True,
            (0,1,1,1):True,

            (-1,0,1,1):False,
            (0,-1,1,1):False,

            (9,0,1,1):True,
            (0,9,1,1):True,
            (10,0,1,1):False,
            (10,10,1,1):False,
            (11,0,1,1):False,
            (0,11,1,1):False,

            (0,0,5,1):True,
            (0,0,1,5):True,
            (0,0,10,1):True,
            (0,0,1,10):True,
            (9,0,2,1):False,
            (0,9,1,2):False,

            (0,8,1,3):False,
            (8,0,3,1):False,
            (0,0,11,1):False,
            (0,0,1,11):False
            }

    for i,j in expected_ship_result.items():
        assert(btl.valid_placement(board,i) == j)

    board = np.array([
            [WTR, WTR, WTR, WTR, WTR ,WTR],
            [WTR, WTR, WTR, WTR, WTR, WTR],
            [WTR, CLR, WTR, CLR, WTR, WTR],
            [WTR, WTR, SHP, WTR, WTR, WTR],
            [WTR, CLR, WTR, CLR, WTR, WTR],
            [WTR, WTR, WTR, WTR, WTR, WTR]
            ])
    expected_ship_result = {
            (0,0,1,1):True,
            (2,3,1,1):True,
            (1,2,1,1):False,
            (2,0,1,5):True,
            (0,2,3,1):False,
            (0,4,2,1):False
            }

    for i,j in expected_ship_result.items():
        assert(btl.valid_placement(board,i) == j)

    print('Valid placement test passed')

test_valid_placement()
