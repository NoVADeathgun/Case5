def check(exam_duration, accommodation, disconnect_duration, login_time, is_PublicHoliday):

    if is_PublicHoliday:
        return "cancelled"
    
    elif login_time > 30:
        return "rejected"
    
    elif disconnect_duration > 5:
        return "auto-submitted"
    
    else:
        return "submitted"