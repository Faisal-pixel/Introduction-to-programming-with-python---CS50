import pytest
from calculator import square

# def main():
#     test_square()

# def test_square():
###### USING JUST ASSERTIONS ############################
#     assert square(2) == 4
#     assert square(3) == 9
#     # assert square(-3) == 9
#     # assert square(0) == 0
#     # assert square(1.5) == 2.25
###### USING IF STATEMENTS ############################
#     # if square(2) != 4:
#     #     print("2 squarred was not 4")
#     # if square(3) != 9:
#     #     print("3 squarred was not 9")

# if __name__ == "__main__":
#     main()

def test_square_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_square_negative():
    assert square(-3) == 9
    assert square(-2) == 4

def test_square_zero():
    assert square(0) == 0

def test_square_str():
    # This passes since it is true, if i pass in a string and try to n * n, a TypeError does get raised
    with pytest.raises(TypeError):
        square("cat")