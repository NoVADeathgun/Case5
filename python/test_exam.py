from exam import check

def test_submitted():
    result = check(120, 0, 0, 1, 0)
    print("status =", result)
    assert result == "submitted"

def test_rejected():
    result = check(120, 0, 0, 50, 0)
    print("status =", result)
    assert result == "rejected"

def test_auto_submitted():
    result = check(120, 0, 30, 0, 0)
    print("status =", result)
    assert result == "auto-submitted"

def test_cancelled():
    result = check(120, 0, 0, 0, 1)
    print("status =", result)
    assert result == "cancelled"