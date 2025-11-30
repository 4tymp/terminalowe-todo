import datetime

from classes import Task
from utils import pull_from_quotes, pull_id

# funkcja zajmujaca sie dodawaniem
def adding(task_input, tasks):
    
    task_desc = pull_from_quotes(task_input) # wyciaga z cudzyslowow tekst

    ## konczy funkcje orzedwczesnie jesli komenda zostala zle wpisana
    if task_desc == None: 
        return None
    
    new_task = Task(len(tasks), task_desc) # tworzy obiekt z nowym taskiem i kolejnym id w kolejce
    
    tasks.append(new_task) #dodaje taska do listy tasks zeby dalo sie ladnie odwolac (id w tasku to index w liscie)
    
    print(f"Pomyślnie dodano task (id: {new_task.id})")

#funkcja zajmujaca sie aktualizowaniem
def updating(task_input, tasks):
    id = pull_id(task_input)

    new_desc = pull_from_quotes(task_input) # wyciaga z cudzyslowow tekst

    ## konczy funkcje orzedwczesnie jesli komenda zostala zle wpisana
    if id == None or new_desc == None:
        return None
    
    tasks[id].desc = new_desc # dodaje nowy opis
    tasks[id].updated_at = datetime.datetime.now()

# funkcja zajmujaca sie usuwaniem
def deleting(task_input, tasks):
    id = pull_id(task_input)

    # failsafe
    if id == None:
        return None
    
    del tasks[id] # usuwanie