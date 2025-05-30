import pytest

# function to check sq
def square(n):
    return n**2

# function to check cube
def cube(n):
    return n**3

# function to check firth power
def fifth_power(n):
    return n**5


# testing the sq fun
def test_square():
    assert square(2) == 4, "Test failed: Sq of the 2 should be 4"
    assert square(3) == 9, "Test failed: Sq of the 3 should be 9"

# testing the cube fun
def test_cube():
    assert cube(2) == 8, "Test failed: Cube of the 2 should be 8"
    assert cube(3) == 27, "Test failed: Cube of the 3 should be 27"


# testing the Fifth Power fun
def test_square():
    assert square(2) == 32, "Test failed: Fifth Power of the 2 should be 32"
    assert square(3) == 243, "Test failed: Fifth Power of the 3 should be 243"

def test_invalid_input():
    with pytest.raises(TypeError):
        square('string')