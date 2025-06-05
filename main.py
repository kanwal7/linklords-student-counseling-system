from appointment import book_session
from slots import get_available_slots
from quote import get_inspirational_quote
from approval import Counselor
from status import update_status
from calendar_view import weekly_calendar_view

def main():
    counselor = Counselor("Dr. Khan")
    session_status = {}

    while True:
        print("\n📘 Student Counseling Appointment System")
        print("1. View Available Slots")
        print("2. Book a Session")
        print("3. Get Inspirational Quote")
        print("4. Counselor Approve/Cancel Session")
        print("5. Update Session Status")
        print("6. View Counselor Calendar")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            slots = get_available_slots()
            print("\nAvailable Time Slots:")
            for slot in slots:
                print(f"- {slot}")

        elif choice == "2":
            name = input("Enter your name: ")
            slot = input("Enter desired time slot (e.g., 10:00 AM): ")
            success = book_session(name, slot)
            if success:
                print("✅ Session booked successfully!")
            else:
                print("❌ That slot is already booked.")

        elif choice == "3":
            quote = get_inspirational_quote()
            print(f"\n🌟 Inspirational Quote:\n\"{quote}\"")

        elif choice == "4":
            slot = input("Enter session slot to approve or cancel: ")
            action = input("Type 'approve' or 'cancel': ")
            if action.lower() == 'approve':
                counselor.approve_session(slot)
                print(f"✅ Session at {slot} approved.")
            elif action.lower() == 'cancel':
                counselor.cancel_session(slot)
                print(f"❌ Session at {slot} cancelled.")

        elif choice == "5":
            slot = input("Enter session time slot: ")
            status = input("Enter status (Completed/Cancelled/Rescheduled): ")
            updated = update_status(session_status, slot, status)
            if updated:
                print("✅ Status updated.")
            else:
                print("❌ Session not found.")

        elif choice == "6":
            print("\n📅 Weekly Calendar View")
            calendar = weekly_calendar_view(counselor.sessions)
            for time, stat in calendar.items():
                print(f"{time}: {stat}")

        elif choice == "7":
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❗ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
