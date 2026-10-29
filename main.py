from display import print_agenda
from planner import StudyPlanner
from sample_data import create_sample_tasks


def main():
    planner = StudyPlanner(create_sample_tasks())
    print_agenda(planner)


if __name__ == "__main__":
    main()
