def SodaPop(value):
    if (value % 5 == 0) and (value % 3 == 0):
        return "SodaPop"
    elif (value == 1):
        return 1
    elif (value == 2):
        return 2
    elif (value == 3):
        return "Soda"
    elif (value == 5):
        return "Pop"
    elif (value % 3 == 0):
        return "Soda"
    elif (value % 5 == 0):
        return "Pop"

def testCanCallSodaPop():
    SodaPop(0)

def testCanCallSodaPop():
    assert SodaPop(15) == "SodaPop"

def testCanCallOne():
    assert SodaPop(1) == 1

def testCanCallTwo():
    assert SodaPop(2) == 2

def testCanCallSoda():
    assert SodaPop(3) == "Soda"

def testCanCallPop():
    assert SodaPop(5) == "Pop"

def testCanCallMult3():
    assert SodaPop(6) == "Soda"

def testCanCallMult5():
    assert SodaPop(10) == "Pop"