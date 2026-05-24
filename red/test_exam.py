from exam import check

def test1():
    result = check(120, 0, 0, 1, 0, 110)
    print("status =", result)
    assert result == "Submitted"

def test2():
    result = check(120, 0, 0, 50, 0, 100)
    print("status =", result)
    assert result == "rejected"

def test3():
    result = check(120, 0, 30, 0, 0, 120)
    print("status =", result)
    assert result == "auto-submitted"

def test4():
    result = check(120, 0, 0, 0, 1, 110)
    print("status =", result)
    assert result == "cancelled"