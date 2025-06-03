from appointment import book_session

def test_book_session_success():
    assert book_session("Ali", "10:00 AM") is True

def test_book_session_already_booked():
    book_session("Ali", "11:00 AM")
    assert book_session("Sara", "11:00 AM") is False
