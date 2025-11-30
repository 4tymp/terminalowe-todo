from classes import Task
from utils import pull_from_quotes, pull_id

# funckja markujaca progress taska
def mark(task_input, tasks, progress):
    id = pull_id(task_input)

    if progress == "in-progress":
        tasks[id].status = "in-progress"
    elif progress == "done":
        tasks[id].status = "done"

# funkcja pokazujaca liste wszystkich taskow
def show_list(tasks):
    print("id | status | opis")

    for i in tasks:
        print(f"{i.id} | {i.status} | {i.desc}")