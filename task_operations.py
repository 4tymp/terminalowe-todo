from classes import Task
from utils import pull_from_quotes, pull_id

def adding(task_input, tasks):
    
    task_desc = pull_from_quotes(task_input) # wyciaga z cudzyslowow tekst

    ## konczy funkcje orzedwczesnie jesli komenda zostala zle wpisana
    if task_desc == None: 
        return None
    
    new_task = Task(len(tasks), task_desc) # tworzy obiekt z nowym taskiem i kolejnym id w kolejce
    
    tasks.append(new_task) #dodaje taska do listy tasks zeby dalo sie ladnie odwolac (id w tasku to index w liscie)
    
    print(f"Pomyślnie dodano task (id: {new_task.id})")


def updating(task_input, tasks):
    id = pull_id(task_input)

    new_desc = pull_from_quotes(task_input) # wyciaga z cudzyslowow tekst

    ## konczy funkcje orzedwczesnie jesli komenda zostala zle wpisana
    if id == None or new_desc == None:
        return None
    print(tasks[id].desc + " przed")
    tasks[id].desc = new_desc

    print(tasks[id].desc + " po")