#bring test in pytest in a virtual enviroment via pip
#define tests with test <whatever here>

def find_largest(x,y):
    if x > y:
        return x
    else:
        return y
def test_find_largest():
    assert find_largest(1,2) == 2

def  test_something():
    assert 'test'

