class Counselor:
    def __init__(self, name):
        self.name = name
        self.sessions = {}

    def approve_session(self, time_slot):
        self.sessions[time_slot] = "Approved"

    def cancel_session(self, time_slot):
        self.sessions[time_slot] = "Cancelled"