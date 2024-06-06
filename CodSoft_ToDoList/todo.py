import pickle

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __repr__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description}"
class ToDoList:
    def __init__(self, filename="tasks.pkl"):
        self.filename = filename
        try:
            with open(self.filename, 'rb') as f:
                self.tasks = pickle.load(f)
        except FileNotFoundError:
            self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        for idx, task in enumerate(self.tasks, start=1):
            print(f"{idx}. {task}")

    def update_task(self, task_id, new_description):
        if 0 < task_id <= len(self.tasks):
            self.tasks[task_id - 1].description = new_description
            self.save_tasks()
        else:
            print("Invalid task ID.")

    def delete_task(self, task_id):
        if 0 < task_id <= len(self.tasks):
            del self.tasks[task_id - 1]
            self.save_tasks()
        else:
            print("Invalid task ID.")

    def mark_task_completed(self, task_id):
        if 0 < task_id <= len(self.tasks):
            self.tasks[task_id - 1].completed = True
            self.save_tasks()
        else:
            print("Invalid task ID.")

    def save_tasks(self):
        with open(self.filename, 'wb') as f:
            pickle.dump(self.tasks, f)
def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task as Complete")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to update: "))
            new_description = input("Enter new description: ")
            todo_list.update_task(task_id, new_description)
        elif choice == "4":
            task_id = int(input("Enter task ID to delete: "))
            todo_list.delete_task(task_id)
        elif choice == "5":
            task_id = int(input("Enter task ID to mark as complete: "))
            todo_list.mark_task_completed(task_id)
        elif choice == "6":
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
