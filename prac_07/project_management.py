"""
CP5632 Practical 7
"""

import datetime
from project import Project
projects = []
def main():
    load_projects()
    print("Welcome to Pythonic Project Management")
    choice = ""
    while choice != " ":
        print( """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
""")
        choice = input(">>> ")
        if choice.lower() == "l":
            file_name = input("Enter file name to load from: ")
            load_projects(file_name)
        elif choice.lower() == "s":
            file_name = input("Enter file name to save to: ")
            save_projects(file_name)
        elif choice.lower() == "d":
            display_projects()
        elif choice.lower() == "f":
            arrange_projects_by_date()
        elif choice.lower() == "a":
            add_new_project()
        elif choice.lower() == "u":
            update_project()
        elif choice.lower() == "q":
            save_option = input(f"Would you like to save to project.txt? : ").lower()
            if save_option.lower() == "y":
                save_projects()
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("This is an invalid choice!")

def load_projects(file_name="projects.txt"):
    try:
        with open(file_name, "r") as file:
            next(file)
            for line in file:
                name, start_date, priority, cost_estimate, completion_percentage = line.strip().split("\t")
                projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
        print(f"Loaded {len(projects)} projects from {file_name}")
    except FileNotFoundError:
        print(f"No file found with name {file_name}.")

def save_projects(file_name="projects.txt"):
    """ Save projects to a file """
    with open(file_name, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    print(f"Saved {len(projects)} projects to {file_name}")

def display_projects():
    incomplete_projects = [project for project in projects if not project.is_complete()]
    completed_projects = [project for project in projects if project.is_complete()]
    print("Incomplete projects:")
    priority_list = []
    for project in incomplete_projects:
        priority_list.append(project.priority)
    sorted_priorities = sorted(priority_list)
    for priority in sorted_priorities:
        for project in incomplete_projects:
            if project.priority == priority:
                print(" ", project)
                break
    print("Completed projects:")
    priority_list = []
    for project in completed_projects:
        priority_list.append(project.priority)
    sorted_priorities = sorted(priority_list)
    for priority in sorted_priorities:
        for project in completed_projects:
            if project.priority == priority:
                print(" ", project)
                break

def arrange_projects_by_date():
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    arrange_projects = [project for project in projects if project.start_date > date]
    for project in arrange_projects:
        print(project)

def add_new_project():
    """ Add a new project """
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate:$ "))
    completion_percentage = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))

def update_project():
    """ Update a project """
    for index, project in enumerate(projects):
        print(f"{index} {project}")
    project_choice = int(input("Project choice: "))
    project = projects[project_choice]
    print(project)
    new_percentage = input("New Percentage: ")
    if new_percentage:
        project.completion_percentage = int(new_percentage)
    new_priority = input("New Priority: ")
    if new_priority:
        project.priority = int(new_priority)



if __name__ == "__main__":
    main()