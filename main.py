import os
from datetime import datetime
import time

# Directory to store diary entries and user data
DIARY_DIR = "diary_entries"
USER_DATA_FILE = "user_data.txt"
EXPORT_FILE = "diary_export.txt"

def get_entry_filename(date):
    """Generate a filename for the entry based on the date."""
    return os.path.join(DIARY_DIR, f"{date}.txt")

def animate_text(text, delay=0.1):
    """Animate text output with a delay."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def write_entry():
    """Allow the user to write a new diary entry or edit an existing one."""
    date = datetime.now().strftime("%Y-%m-%d")
    entry_filename = get_entry_filename(date)
    
    if os.path.exists(entry_filename):
        animate_text(f"\nAn entry for {date} already exists.")
        edit_choice = input("Do you want to edit it? (y/n): ")
        if edit_choice.lower() == 'y':
            edit_entry(entry_filename)
        else:
            animate_text("Entry not modified.")
    else:
        with open(entry_filename, "w") as file:
            animate_text(f"\nWriting entry for {date}:")
            entry = input("Write your thoughts: ")
            file.write(f"{entry}\n")
        animate_text("Entry saved!")

def edit_entry(entry_filename):
    """Allow the user to edit an existing diary entry."""
    with open(entry_filename, "r") as file:
        current_content = file.read()
    
    animate_text(f"\nCurrent entry for {entry_filename.split('/')[-1].replace('.txt', '')}:\n{current_content}")
    new_content = input("Enter new content: ")
    
    with open(entry_filename, "w") as file:
        file.write(f"{new_content}\n")
    animate_text("Entry updated!")

def delete_entry():
    """Allow the user to delete a diary entry."""
    date = input("Enter the date of the entry to delete (YYYY-MM-DD): ")
    entry_filename = get_entry_filename(date)
    
    if os.path.exists(entry_filename):
        os.remove(entry_filename)
        animate_text(f"Entry for {date} deleted.")
    else:
        animate_text(f"No entry found for {date}.")

def view_entries():
    """View diary entries for a specific date or all entries."""
    date = input("Enter date to view entries (YYYY-MM-DD) or press Enter to view all: ")
    
    if date:
        entry_filename = get_entry_filename(date)
        if os.path.exists(entry_filename):
            with open(entry_filename, "r") as file:
                animate_text(f"\nDate: {date}")
                print(file.read())
        else:
            animate_text(f"No entry found for {date}.")
    else:
        animate_text("\n--- Your Diary Entries ---\n")
        if not os.listdir(DIARY_DIR):
            animate_text("No entries found.")
            return
        
        for filename in os.listdir(DIARY_DIR):
            with open(os.path.join(DIARY_DIR, filename), "r") as file:
                date = filename.replace(".txt", "")
                animate_text(f"\nDate: {date}")
                print(file.read())
                print("-" * 40)

def search_entries():
    """Search diary entries by date range or keywords."""
    search_term = input("Enter a keyword to search or 'date range' to search by date range: ")
    if search_term.lower() == 'date range':
        start_date = input("Enter start date (YYYY-MM-DD): ")
        end_date = input("Enter end date (YYYY-MM-DD): ")
        search_by_date_range(start_date, end_date)
    else:
        search_by_keyword(search_term)

def search_by_keyword(keyword):
    """Search diary entries by keyword."""
    found = False
    
    for filename in os.listdir(DIARY_DIR):
        with open(os.path.join(DIARY_DIR, filename), "r") as file:
            content = file.read()
            if keyword in filename or keyword in content:
                date = filename.replace(".txt", "")
                animate_text(f"\nDate: {date}")
                print(content)
                print("-" * 40)
                found = True
    
    if not found:
        animate_text("No entries found matching your search.")

def search_by_date_range(start_date, end_date):
    """Search diary entries within a date range."""
    found = False
    
    for filename in os.listdir(DIARY_DIR):
        date = filename.replace(".txt", "")
        if start_date <= date <= end_date:
            with open(os.path.join(DIARY_DIR, filename), "r") as file:
                animate_text(f"\nDate: {date}")
                print(file.read())
                print("-" * 40)
                found = True
    
    if not found:
        animate_text("No entries found within the specified date range.")

def export_entries():
    """Export all diary entries to a text file."""
    with open(EXPORT_FILE, "w") as outfile:
        for filename in os.listdir(DIARY_DIR):
            with open(os.path.join(DIARY_DIR, filename), "r") as infile:
                date = filename.replace(".txt", "")
                outfile.write(f"Date: {date}\n")
                outfile.write(infile.read())
                outfile.write("\n" + ("-" * 40) + "\n")
    animate_text(f"All entries have been exported to {EXPORT_FILE}.")

def authenticate_user():
    """Authenticate the user by checking credentials."""
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if not os.path.exists(USER_DATA_FILE):
        return False
    
    with open(USER_DATA_FILE, "r") as file:
        for line in file:
            saved_username, saved_password = line.strip().split(":")
            if saved_username == username and saved_password == password:
                return True
    
    return False

def register_user():
    """Register a new user by saving their credentials."""
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    
    with open(USER_DATA_FILE, "a") as file:
        file.write(f"{username}:{password}\n")
    animate_text("Registration successful!")

def diary_menu():
    """Display the diary menu and handle user input."""
    if not authenticate_user():
        animate_text("Invalid username or password. Exiting...")
        return
    
    while True:
        print("\n--- Personal Diary Menu ---")
        print("1. Write a new entry")
        print("2. Edit an existing entry")
        print("3. Delete an entry")
        print("4. View entries")
        print("5. Search entries")
        print("6. Export all entries")
        print("7. Exit")
        
        choice = input("Choose an option (1-7): ")
        
        if choice == "1":
            write_entry()
        elif choice == "2":
            date = input("Enter the date of the entry to edit (YYYY-MM-DD): ")
            edit_entry(get_entry_filename(date))
        elif choice == "3":
            delete_entry()
        elif choice == "4":
            view_entries()
        elif choice == "5":
            search_entries()
        elif choice == "6":
            export_entries()
        elif choice == "7":
            animate_text("Exiting... Goodbye!")
            break
        else:
            animate_text("Invalid option. Please try again.")

def main():
    """Main function to handle registration and login."""
    while True:
        print("\n--- Personal Diary Application ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            register_user()
        elif choice == "2":
            diary_menu()
            break
        elif choice == "3":
            animate_text("Exiting... Goodbye!")
            break
        else:
            animate_text("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
