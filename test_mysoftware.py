from mysoftware import *

def test_square_integers():
	assert square(2) == 4
	assert square(0) == 0
	assert square(-1) == 1
	assert square(3) == 9

def test_exponent():
	assert EXPO(2,3) == 8
	assert EXPO(2,4) == 16