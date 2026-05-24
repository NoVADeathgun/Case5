def check_holiday (is_PublicHoliday):
    if is_PublicHoliday == 1:
        return "Canceled" 

def check_logintime (login_time):
    if login_time > 30:
        return "Rejected"

def check_disconnect (disconnect_duration):
    if disconnect_duration > 5:
        return "Auto-Submitted"

def check_duration (exam_duration, accommodation):
    if accommodation == 1:
        return exam_duration + 30
    else:
        return exam_duration
    
def check_eligible (exam_duration, exam_time):
    if exam_duration >= exam_time:
        return "Submitted"
    else:
        return "Rejected"


def check(exam_duration, accommodation, disconnect_duration, login_time, is_PublicHoliday, exam_time):

    return -1
    

