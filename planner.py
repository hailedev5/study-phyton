class StudyPlanner:
    """Manage study tasks and retrieve them in deadline order."""

    def __init__(self, tasks=None):
        self._tasks = list(tasks) if tasks is not None else []

    def add_task(self, task):
        self._tasks.append(task)

    def all_tasks(self):
        return list(self._tasks)

    def pending_tasks(self):
        return sorted(
            (task for task in self._tasks if not task.is_complete),
            key=lambda task: (task.due_date, task.title.lower())
        )

    def complete_task(self, title):
        """Complete a pending task by title; return False if it was not found."""
        query = title.strip().lower()
        for task in self._tasks:
            if task.title.lower() == query and not task.is_complete:
                task.is_complete = True
                return True
        return False
