class StudyTask:
    """A study task with a due date and estimated workload."""

    def __init__(self, title, subject, due_date, estimated_minutes):
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty.")
        if not subject or not subject.strip():
            raise ValueError("Task subject cannot be empty.")
        if not isinstance(estimated_minutes, int) or estimated_minutes < 0:
            raise ValueError("Estimated minutes must be a non-negative integer.")

        self.title = title.strip()
        self.subject = subject.strip()
        self.due_date = due_date
        self.estimated_minutes = estimated_minutes
        self.is_complete = False
