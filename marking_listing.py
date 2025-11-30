from classes import Task
from utils import pull_from_quotes, pull_id

# funckja markujaca in progress taska
def mark_in_progress(task_input, tasks):
    id = pull_id(task_input)

    tasks[id].status = "in-progress"

# funckja markujaca taska jako done
def mark_done(task_input, tasks):
    id = pull_id(task_input)

    tasks[id].status = "done"