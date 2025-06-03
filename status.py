def update_status(session_dict, time_slot, status):
    if time_slot in session_dict:
session_dict[time_slot] = status
        return True
    return False
