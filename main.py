from menu import display_menu, get_user_choice, clear_screen
from todos import input_task, add_task, view_tasks, mask_task_completion,\
    delete_task, clear_all_tasks, search_task,sort_tasks, save_tasks_to_file, load_tasks_from_file   

def main():
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 0:
            print("Exiting the application. Goodbye!")
            break
        print('-' * 40)
        if choice == 1:
        
            print("Add a new task selected.")
            name, due_date, priority, status = input_task()
            add_task(name, due_date, priority, status)
            print(f"Task '{name}' added successfully.")
            
        elif choice == 2:
            print("View all tasks selected.")
            view_tasks()
        elif choice == 3:
            print("Mark a task as completed selected.")
            task_id = int(input("Enter the task ID to mark as completed: "))
            mask_task_completion(task_id)
        elif choice == 4:
            print("Delete a task selected.")
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)
        elif choice == 5:
            print("Clear all tasks selected.")
            clear_all_tasks()
        elif choice == 6:
            print("Search for a task selected.")
            query = input("Enter the search query: ")
            search_task(query)
        elif choice == 7:
            print("Sort tasks selected.")
            sort_choice = input("Sort by (Name, Due Date, Priority): ").strip().lower()
            if sort_choice in ['name', 'due date', 'priority']:
                sort_tasks(sort_choice)
                print(f"Tasks sorted by {sort_choice}.")
            else:
                print("Invalid sort option. Please choose Name, Due Date, or Priority.")
        elif choice == 8:
            print("Save tasks to file selected.")
            save_tasks_to_file()
        elif choice == 9:
            print("Load tasks from file selected.")
            load_tasks_from_file()
        print('\n\n')
        print('-' * 40)
        input("Press Enter to continue...")
        clear_screen()
            
    
if __name__ == "__main__":
    main()