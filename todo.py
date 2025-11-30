
from classes import Task
from functions import adding

tasks = []


while True:
    task_input = input(">>> ")

    # sprawdza tekst w koemndzie ktora wpisujemy
    if task_input.startswith("add "): #jezeli zaczyna sie z add
        adding(task_input, tasks)
    
    if task_input.startswith("update "): # jezeli zaczyna sie z update
        x = 2

    if task_input == "quit":
        break