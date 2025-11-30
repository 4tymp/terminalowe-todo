
from classes import Task
from utils import save, load
from task_operations import adding, updating, deleting
from marking_listing import mark, show_list

tasks = load() ## lista nam potrzebna do mozliwosci dzialania na obiektoach!


while True:
    task_input = input(">>> ")

    # sprawdza tekst w koemndzie ktora wpisujemy
    if task_input.startswith("add "): #jezeli zaczyna sie z add
        adding(task_input, tasks)
        save(tasks)

    elif task_input.startswith("update "): # jezeli zaczyna sie z update
        updating(task_input, tasks)
        save(tasks)

    elif task_input.startswith("delete "): # jezeli zaczyna sie z delete
        deleting(task_input, tasks)
        save(tasks)

    elif task_input.startswith("mark-in-progress "): # jezeli zaczyna sie z mark-in-progress
        mark(task_input, tasks, "in-progress")
        save(tasks)

    elif task_input.startswith("mark-done "): # jezeli zaczyna sie z mark-done
        mark(task_input, tasks, "done")
        save(tasks)

    elif task_input.startswith("list"): # jezeli zaczyna sie z list
        show_list(task_input, tasks)

    elif task_input == "quit":
        save(tasks)
        break