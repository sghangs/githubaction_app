from src.math_operation import add,sub

def test_add(a,b):
    assert add(2,3)==5
    assert add(5,-7)==-2

def test_sub(a,b):
    assert sub(4,1)==3
    assert sub(5,7)==-2

    