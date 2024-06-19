class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = "Incomplete"

    def mark_as_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {self.status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return True
        return False

    def get_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def get_all_tasks(self):
        return self.tasks

# Example usage:
if __name__ == "__main__":
    task_manager = TaskManager()

    task1 = Task("Complete Python Project", "Finish the Python project on time.", "2023-09-30")
    task2 = Task("Learn OOP Concepts", "Study object-oriented programming concepts in Python.", "2023-10-15")

    task_manager.add_task(task1)
    task_manager.add_task(task2)

    print("All Tasks:")
    for task in task_manager.get_all_tasks():
        print(task)

    task_manager.remove_task("Complete Python Project")

    print("\nRemaining Tasks:")
    for task in task_manager.get_all_tasks():
        print(task)
