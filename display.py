from datetime import date


def print_agenda(planner):
    """Print pending tasks in deadline order and summarize study time."""
    tasks = planner.pending_tasks()
    print("STUDY PLANNER")
    print("=" * 72)

    if not tasks:
        print("You're all caught up. No pending study tasks!")
        return

    total_minutes = sum(task.estimated_minutes for task in tasks)
    print("{:<12} {:<13} {:<30} {:>8}  {}".format(
        "Due", "Status", "Task", "Minutes", "Subject"
    ))
    print("-" * 72)

    today = date.today()
    for task in tasks:
        days_until_due = (task.due_date - today).days
        if days_until_due < 0:
            status = "OVERDUE"
        elif days_until_due == 0:
            status = "TODAY"
        else:
            status = "IN {} DAYS".format(days_until_due)

        print("{:<12} {:<13} {:<30} {:>8}  {}".format(
            task.due_date.strftime("%b %d"), status, task.title[:30],
            task.estimated_minutes, task.subject
        ))

    hours, minutes = divmod(total_minutes, 60)
    print("-" * 72)
    print("{} pending tasks | Estimated study time: {}h {}m".format(
        len(tasks), hours, minutes
    ))
