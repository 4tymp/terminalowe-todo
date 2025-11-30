import datetime

from classes import Task
from utils import pull_id, pull_status

# funckja markujaca progress taska
def mark(task_input, tasks, progress):
    id = pull_id(task_input)

    if progress == "in-progress":
        tasks[id].status = "in-progress"
    elif progress == "done":
        tasks[id].status = "done"

    tasks[id].updated_at = datetime.datetime.now()


#funkcja pokazujaca wybrana liste wedlug statusu
def show_list(task_input, tasks):
    status = pull_status(task_input)

    if status == None:
        return None
    # failsafe
    
    print("id | status | opis")
        
    for i in tasks:
        if status == "samo" or i.status == status:
            print(f"{i.id} | {i.status} | {i.desc}")


