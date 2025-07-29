##  heres my project ##







import calendar
import os
from datetime import datetime

class CalendarNotesApp:
    def __init__(self, notes_dir="notes"):
        self.notes_dir = notes_dir
        os.makedirs(self.notes_dir, exist_ok=True)

    def show_calendar(self):
        """Display calendar with today highlighted (if in same month/year)"""
        try:
            year = int(input("Enter year (e.g., 2025): "))
            month = int(input("Enter month (1-12): "))
            today = datetime.now()

            print(f"\n{'='*30}")
            print(f"Calendar for {calendar.month_name[month]} {year}".center(30))
            print(f"{'='*30}\n")
            print(" Mo Tu We Th Fr Sa Su")

            cal = calendar.monthcalendar(year, month)
            for week in cal:
                week_str = ""
                for day in week:
                    if day == 0:
                        week_str += "   "
                    elif day == today.day and month == today.month and year == today.year:
                        week_str += f"[\033[1;31m{day:2}\033[0m]"
                    else:
                        week_str += f" {day:2}"
                print(week_str)
        except Exception as e:
            print(f"Error showing calendar: {e}")

    def add_note(self):
        """Add a note for a specific date"""
        try:
            date_input = input("Enter date (YYYY_MM_DD) or 'today': ").lower()
            if date_input == 'today':
                date_str = datetime.now().strftime("%Y_%m_%d")
            else:
                try:
                    date_str = datetime.strptime(date_input, "%Y_%m_%d").strftime("%Y_%m_%d")
                except ValueError:
                    print("Invalid date format.")
                    return

            note = input("Write your note: ")
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            note_with_time = f"[{timestamp}] {note}\n"

            with open(f"{self.notes_dir}/{date_str}.txt", "a") as f:
                f.write(note_with_time)

            print(f"✅ Note saved for {date_str}")
        except Exception as e:
            print(f"Error adding note: {e}")

    def view_notes(self):
        """View notes for a date or list all available notes"""
        try:
            option = input("1. View specific date\n2. List all notes\nChoose option (1/2): ")

            if option == '1':
                date_input = input("Enter date (YYYY_MM_DD) or 'today': ").lower()
                if date_input == 'today':
                    date_str = datetime.now().strftime("%Y_%m_%d")
                else:
                    try:
                        date_str = datetime.strptime(date_input, "%Y_%m_%d").strftime("%Y_%m_%d")
                    except ValueError:
                        print("Invalid date format.")
                        return

                filepath = f"{self.notes_dir}/{date_str}.txt"
                if os.path.exists(filepath):
                    print(f"\n📅 Notes for {date_str}")
                    print("-" * 40)
                    with open(filepath, "r") as f:
                        print(f.read())
                    print("-" * 40)
                else:
                    print("❌ No notes for this date.")
            elif option == '2':
                print("\n🗓️ Dates with notes:")
                print("-" * 30)
                files = sorted(os.listdir(self.notes_dir))
                if not files:
                    print("No notes found.")
                for f in files:
                    if f.endswith(".txt"):
                        print(f"- {f.replace('.txt', '')}")
            else:
                print("Invalid option.")
        except Exception as e:
            print(f"Error viewing notes: {e}")

    def delete_note(self):
        """Delete all notes for a specific date"""
        try:
            date = input("Enter date to delete (YYYY_MM_DD): ")
            filepath = f"{self.notes_dir}/{date}.txt"

            if os.path.exists(filepath):
                confirm = input(f"Are you sure to delete all notes for {date}? (y/n): ").lower()
                if confirm == 'y':
                    os.remove(filepath)
                    print(f"🗑️ All notes for {date} deleted.")
            else:
                print("No notes found.")
        except Exception as e:
            print(f"Error deleting note: {e}")

    def search_notes(self):
        """Search across all notes by keyword"""
        try:
            keyword = input("Enter keyword to search: ").lower()
            found = False

            print("\n🔍 Search Results:")
            print("-" * 50)
            for filename in os.listdir(self.notes_dir):
                if filename.endswith(".txt"):
                    date = filename.replace(".txt", "")
                    with open(os.path.join(self.notes_dir, filename), "r") as f:
                        lines = f.readlines()
                        for line in lines:
                            if keyword in line.lower():
                                print(f"📅 {date}")
                                print(f"📝 {line.strip()}")
                                print("-" * 50)
                                found = True

            if not found:
                print("No matching notes found.")
        except Exception as e:
            print(f"Error searching notes: {e}")

    def run(self):
        """Main loop for the menu interface"""
        while True:
            print("\n" + "=" * 40)
            print(" BEAUTIFUL CALENDAR & NOTES ".center(40, "="))
            print("=" * 40)
            print("1. Show Calendar")
            print("2. Add Note")
            print("3. View Notes")
            print("4. Delete Notes")
            print("5. Search Notes")
            print("6. Exit")

            choice = input("\nSelect option (1–6): ")
            if choice == '1':
                self.show_calendar()
            elif choice == '2':
                self.add_note()
            elif choice == '3':
                self.view_notes()
            elif choice == '4':
                self.delete_note()
            elif choice == '5':
                self.search_notes()
            elif choice == '6':
                print("✅ Exiting... will met soon  thank yoy !")
                break
            else:
                print("Invalid input. Please try again.")

if __name__ == "__main__":
    app = CalendarNotesApp()
    app.run()