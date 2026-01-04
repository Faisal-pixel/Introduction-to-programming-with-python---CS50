from hello import hello

######## Testing all inside one function ######

def test_hello():
    assert hello("David") == "hello, David"
    assert hello() == "hello, world"

######### BUT IT IS BEST PRACTICE TO SEPERATE TEST FUNCTIONS ##########

def test_hello_default():
    assert hello() == "hello, world"

def test_hello_argument():
    assert hello("David") == "hello, David"