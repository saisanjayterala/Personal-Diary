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
    """Allow the user to write a new diary entry or edit an existing one."""
    date = datetime.now().strftime("%Y-%m-%d")
    entry_filename = get_entry_filename(date)
    
    if os.path.exists(entry_filename):
        print(f"An entry for {date} already exists.")
        edit_choice = input("Do you want to edit it? (y/n): ")
        if edit_choice.lower() == 'y':
            edit_entry(entry_filename)
        else:
            print("Entry not modified.")
    else:
        with open(entry_filename, "w") as file:
            print(f"\nWriting entry for {date}:")
            entry = input("Write your thoughts: ")
            file.write(f"{entry}\n")
        print("Entry saved!")

def edit_entry(entry_filename):
    """Allow the user to edit an existing diary entry."""
    with open(entry_filename, "r") as file:
        current_content = file.read()
    
    print(f"\nCurrent entry for {entry_filename.split('/')[-1].replace('.txt', '')}:\n{current_content}")
    new_content = input("Enter new content: ")
    
    with open(entry_filename, "w") as file:
        file.write(f"{new_content}\n")
    print("Entry updated!")

def delete_entry():
    """Allow the user to delete a diary entry."""
    date = input("Enter the date of the entry to delete (YYYY-MM-DD): ")
    entry_filename = get_entry_filename(date)
    
    if os.path.exists(entry_filename):
        os.remove(entry_filename)
        print(f"Entry for {date} deleted.")
    else:
        print(f"No entry found for {date}.")

def view_entries():
    """View all diary entries."""
    print("\n--- Your Diary Entries ---\n")
    
    if not os.listdir(DIARY_DIR):
        print("No entries found.")
        return
    
    for filename in os.listdir(DIARY_DIR):
        with open(os.path.join(DIARY_DIR, filename), "r") as file:
            date = filename.replace(".txt", "")
            print(f"Date: {date}")
            print(file.read())
            print("-" * 40)

def search_entries():
    """Search diary entries by date or keywords."""
    search_terms = input("Enter date (YYYY-MM-DD) or keywords to search: ").split()
    found = False
    
    for filename in os.listdir(DIARY_DIR):
        with open(os.path.join(DIARY_DIR, filename), "r") as file:
            content = file.read()
            if any(term in filename or term in content for term in search_terms):
                date = filename.replace(".txt", "")
                print(f"\nDate: {date}")
                print(content)
                print("-" * 40)
                found = True
    
    if not found:
        print("No entries found matching your search.")

def diary_menu():
    """Display the diary menu and handle user input."""
    while True:
        print("\n--- Personal Diary Menu ---")
        print("1. Write a new entry")
        print("2. Edit an existing entry")
        print("3. Delete an entry")
        print("4. View all entries")
        print("5. Search entries")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ")
        
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
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Start the diary application
if __name__ == "__main__":
    diary_menu()
