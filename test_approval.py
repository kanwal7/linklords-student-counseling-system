from approval import Counselor
def test_approve_session():
    c = Counselor("Dr. Khan")
    c.approve_session("10:00 AM")
    assert c.sessions["10:00 AM"] == "Approved"

def test_cancel_session():
    c = Counselor("Dr. Khan")
    c.cancel_session("11:00 AM")
    assert c.sessions["11:00 AM"] == "Cancelled"