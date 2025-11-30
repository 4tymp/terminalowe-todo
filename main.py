
from classes import Task
from task_operations import adding, updating

tasks = []


while True:
    task_input = input(">>> ")

    # sprawdza tekst w koemndzie ktora wpisujemy
    if task_input.startswith("add "): #jezeli zaczyna sie z add
        adding(task_input, tasks)
    
    if task_input.startswith("update "): # jezeli zaczyna sie z update
        updating(task_input, tasks)

    if task_input == "quit":
        break