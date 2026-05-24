from src.exam_system import check_exam_status

def test_public_holiday_exam_canceled():
    assert check_exam_status(60, False, 0, 10, True) == "Canceled"

def test_public_holiday_with_accommodation_canceled():
    assert check_exam_status(150, True, 0, 5, True) == "Canceled"

def test_public_holiday_with_disconnect_canceled():
    assert check_exam_status(60, False, 6, 10, True) == "Canceled"

def test_public_holiday_with_late_login_canceled():
    assert check_exam_status(60, False, 0, 35, True) == "Canceled"