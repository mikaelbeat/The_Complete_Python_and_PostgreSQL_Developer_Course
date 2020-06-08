
from database import add_entry, get_entries

menu = """\nPlease select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

welcome = "Welcome to the programming diary!"

def promt_new_entry():
        entry_content = input("What have you learned today? ")
        entry_date = input("Enter the date: ")
        add_entry(entry_content, entry_date)

def view_entries():
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


user_input = input(menu)
while user_input != "3":

    user_input = input(menu)

    if user_input == "1":
        promt_new_entry()

    elif user_input == "2":
        view_entries(get_entries())

    
    elif user_input == "3":
        print("Exiting app...")
    else:
        print("Invalid choice, please try again.")
