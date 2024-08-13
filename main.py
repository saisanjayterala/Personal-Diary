import os
from datetime import datetime

# Directory to store diary entries
DIARY_DIR = "diary_entries"

# Ensure the directory exists
if not os.path.exists(DIARY_DIR):
    os.makedirs(DIARY_DIR)

def get_entry_filename(date):
    """Generate a filename for the entry based on the date."""
    return os.path.join(DIARY_DIR, f"{date}.txt")

def write_entry():
    """Allow the user to write a new diary entry."""
    date = datetime.now().strftime("%Y-%m-%d")
    entry_filename = get_entry_filename(date)
    
    with open(entry_filename, "a") as file:
        print(f"Write your entry for {date}:")
        entry = input(">>> ")
        file.write(f"{entry}\n")
    print("Entry saved successfully!")

def view_entries():
    """View all diary entries."""
    print("Your diary entries:\n")
    
    for filename in os.listdir(DIARY_DIR):
        with open(os.path.join(DIARY_DIR, filename), "r") as file:
            date = filename.replace(".txt", "")
            print(f"Date: {date}")
            print(file.read())
            print("-" * 40)

def search_entries():
    """Search diary entries by date or keywords."""
    search_term = input("Enter date (YYYY-MM-DD) or keyword to search: ")
    found = False
    
    for filename in os.listdir(DIARY_DIR):
        with open(os.path.join(DIARY_DIR, filename), "r") as file:
            content = file.read()
            if search_term in filename or search_term in content:
                date = filename.replace(".txt", "")
                print(f"Date: {date}")
                print(content)
                print("-" * 40)
                found = True
    
    if not found:
        print("No entries found matching your search.")

def diary_menu():
    """Display the diary menu and handle user input."""
    while True:
        print("\nPersonal Diary Menu:")
        print("1. Write a new entry")
        print("2. View all entries")
        print("3. Search entries")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            print("Exiting the diary. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the diary application
if __name__ == "__main__":
    diary_menu()
