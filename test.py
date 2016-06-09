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

def test_combinations():
    board = np.array([
            [WTR, WTR, WTR, WTR, WTR, WTR],
            [WTR, WTR, WTR, WTR, WTR, WTR],
            [WTR, CLR, WTR, CLR, WTR, WTR],
            [WTR, WTR, SHP, WTR, WTR, WTR],
            [WTR, CLR, WTR, CLR, WTR, WTR],
            [WTR, WTR, WTR, WTR, WTR, WTR]
            ])

    expected_ship_result = {
            (0,0,1):set([(0,0,1,1)]),
            (0,0,3):set([(0,0,3,1),(0,0,1,3)]),
            (1,0,3):set([(0,0,3,1),(1,0,3,1)]),
            }
    
    for ii,jj in expected_ship_result.items():
        assert(btl.valid_combinations(board,*ii) == jj)
    print('Combination test passed')

def test_combo_grid():
    board = np.array([
        [WTR, WTR, WTR, WTR, WTR, WTR],
        [WTR, WTR, WTR, WTR, WTR, WTR],
        [WTR, WTR, CLR, WTR, CLR, WTR],
        [WTR, WTR, WTR, SHP, WTR, WTR],
        [WTR, WTR, CLR, WTR, CLR, WTR],
        [WTR, WTR, WTR, WTR, WTR, WTR],
        [WTR, WTR, WTR, WTR, WTR, WTR],
        [WTR, WTR, WTR, WTR, WTR, WTR]
        ])
    expected_combo = np.array([[6., 9., 9., 11., 7., 6.],
            [  9.,  12.,   9.,  14.,   7.,   9.],
            [  9.,   9.,   0.,   8.,   0.,   8.],
            [ 12.,  15.,   8.,  17.,   6.,  12.],
            [ 10.,  10.,   0.,   9.,   0.,   9.],
            [ 11.,  14.,  10.,  16.,   8.,  11.],
            [  9.,  12.,  11.,  14.,   9.,   9.],
            [  6.,   9.,  10.,  11.,   8.,   6.]])

    assert(np.array_equal(btl.combo_grid(board,set([2,3,4])), expected_combo))

test_valid_placement()
test_combinations()
test_combo_grid()
