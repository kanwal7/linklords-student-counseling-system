from slots import get_available_slots
def test_get_available_slots():
    available = get_available_slots()
    assert "9:00 AM" in available
    assert "10:00 AM" not in available

