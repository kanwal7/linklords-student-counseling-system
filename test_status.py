from status import update_status
def test_update_completed():
    sessions = {"10:00 AM": "Approved"}
    assert update_status(sessions, "10:00 AM", "Completed")
    assert sessions["10:00 AM"] == "Completed"