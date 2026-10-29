from datetime import date, timedelta

from task import StudyTask


def create_sample_tasks():
    """Create example tasks with deadlines relative to today."""
    today = date.today()
    return [
        StudyTask("Review algebra notes", "Math", today, 45),
        StudyTask("Write history outline", "History", today + timedelta(days=2), 60),
        StudyTask("Practice vocabulary", "Spanish", today + timedelta(days=1), 25),
        StudyTask("Read biology chapter", "Biology", today + timedelta(days=5), 40),
    ]
