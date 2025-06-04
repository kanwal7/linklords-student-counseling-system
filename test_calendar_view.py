from calendar_view import weekly_calendar_view
def test_calendar_output():
    sessions = {
        "Mon 10:00 AM": "Completed",
        "Tue 11:00 AM": "Cancelled"
    }
    calendar = weekly_calendar_view(sessions)
    assert calendar["Mon 10:00 AM"] == "Completed"
    assert calendar["Tue 11:00 AM"] == "Cancelled"