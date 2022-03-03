from app.folder00.calculator import Calculator

cal = Calculator()

def test_add():
    assert cal.add(1,1) == 2
    assert cal.add(1,2) == 3

def test_subtract():

    assert cal.subtract(2,1) == 1
    assert cal.subtract(4,2) == 2
    assert cal.subtract(5,1) == 4
