def display_menu():
    print("Welcome to the Todo Application!")
    print("please choose an option:")
    print("1. Add a new task")
    print("2. View all tasks")  
    print("3. Mark a task as completed")   
    print("4. Delete a task")
    print("5. Clear all tasks")
    print("6. Search for a task")
    print("7. Sort tasks")
    print("8. Save tasks to file")
    print("9. Load tasks from file")
    print("0. Exit")    
 
def clear_screen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
 
def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 0 <= choice <= 9:
                return choice
            else:
                print("Invalid choice. Please enter a number between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            input("Press Enter to continue...")
            clear_screen()