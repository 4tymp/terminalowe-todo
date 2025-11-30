
from classes import Task
from task_operations import adding, updating, deleting
from marking_listing import mark_in_progress, mark_done

tasks = [] ## lista nam potrzebna do mozliwosci dzialania na obiektoach!


while True:
    task_input = input(">>> ")

    # sprawdza tekst w koemndzie ktora wpisujemy
    if task_input.startswith("add "): #jezeli zaczyna sie z add
        adding(task_input, tasks)
    
    if task_input.startswith("update "): # jezeli zaczyna sie z update
        updating(task_input, tasks)

    if task_input.startswith("delete "): # jezeli zaczyna sie z delete
        deleting(task_input, tasks)

    if task_input.startswith("mark-in-progress "): # jezeli zaczyna sie z mark-in-progress
        mark_in_progress(task_input, tasks)

    if task_input.startswith("mark-done "): # jezeli zaczyna sie z mark-done
        mark_done(task_input, tasks)

    if task_input == "quit":
        break