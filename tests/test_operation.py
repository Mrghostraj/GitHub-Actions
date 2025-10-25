from src.maths_operation import add, sub, mult

def test_add():
    assert add(2, 3)==5
    assert add(3,4)==7
    assert add(1,2)==3 
    assert add(6,8)==14 
    
def test_sub():
    assert sub(3,2)==1
    assert sub(6,4)==2
    assert sub(1,2)==-1
    assert sub(6,8)==-2
    
def test_mult():
    assert mult(3,2)==6
    assert mult(6,4)==24
    assert mult(1,2)==2
    assert mult(6,8)==48
    
    