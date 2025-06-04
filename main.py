from slots import get_available_slots
from appointment import book_session
from approval import Counselor
from quote import get_inspirational_quote
from status import update_status
from calendar_view import weekly_calendar_view

def main():
    print("\n📅 Available Time Slots:")
    available = get_available_slots()
    for slot in available:
        print(f"- {slot}")

    print("\n🧑 Student Booking Session...")
    student_name = "Areeba"
    time_slot = "9:00 AM"
    if book_session(student_name, time_slot):
        print(f"✅ {student_name} successfully booked {time_slot}")
    else:
        print(f"❌ Failed to book {time_slot}")

    print("\n👨‍⚕️ Counselor Approving Session...")
    counselor = Counselor("Dr. Fatima")
    counselor.approve_session(time_slot)
    print(f"Approved Sessions: {counselor.sessions}")

    print("\n⏳ Updating Session Status...")
    update_status(counselor.sessions, time_slot, "Completed")
    print(f"Updated Sessions: {counselor.sessions}")

    print("\n💡 Inspirational Quote for Student:")
    print(f"👉 {get_inspirational_quote()}")

    print("\n📆 Counselor's Weekly Calendar:")
    calendar = weekly_calendar_view(counselor.sessions)
    for day, status in calendar.items():
        print(f"{day}: {status}")

if __name__ == "__main__":
    main()
