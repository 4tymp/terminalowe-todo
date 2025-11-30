from classes import Task
from utils import pull_from_quotes

def adding(task_input, tasks):
    #wyciagamy srodek cudzyslowia
    if "\"" in task_input: # \" - cudzyslow w pythonie ziomek
            task_desc = pull_from_quotes(task_input)       
            
            new_task = Task(len(tasks), task_desc) # tworzy obiekt z nowym taskiem i kolejnym id w kolejce
            
            tasks.append(new_task) #dodaje taska do listy tasks zeby dalo sie ladnie odwolac (id w tasku to index w liscie)
            
            print(f"Pomyślnie dodano task (id: {new_task.id})")


def updating(task_input, tasks):
    print("chuj")