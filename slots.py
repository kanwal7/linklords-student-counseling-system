appointments = {
    "9:00 AM": None,
    "10:00 AM": "Ali",
    "11:00 AM": None,
    "12:00 PM": "Sara"
}

def get_available_slots():
    return [slot for slot, user in appointments.items() if user is None]
