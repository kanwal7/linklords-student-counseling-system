appointments = {}

def book_session(student_name, time_slot):
    if time_slot not in appointments:
        appointments[time_slot] = student_name
        return True
    return False