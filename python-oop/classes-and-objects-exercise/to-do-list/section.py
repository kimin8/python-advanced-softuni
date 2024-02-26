from task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task) -> str:
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str) -> str:
        if task_name in self.tasks:
            task_name.completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self) -> str:
        first_len = len(self.tasks)
        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
        second_len = len(self.tasks)
        return f"Cleared {first_len - second_len} tasks."

    def view_section(self) -> str:
        message_to_return = f"Section {self.name}:"
        for item in self.tasks:
            message_to_return += f"\n{item.details()}"
        return message_to_return
