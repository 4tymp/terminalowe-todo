from classes import Task

def adding(task, tasks):
    #wyciagamy srodek cudzyslowia
    if "\"" in task: # \" - cudzyslow w pythonie ziomek
        first_quote = task.find("\"") # pierwszego cudzyslowia szuka
        second_quote = task.rfind("\"") # ostatniego cudzyslowia szuka
        
        if first_quote < second_quote:    
            task_desc = task[first_quote+1: second_quote] # wrzuca do zmiennej task_descr to co jest pomiedzy cudzyslowami (dajemy +1 zeby nie zaczelo od cudzyslowia)
            
            new_task = Task(len(tasks), task_desc) # tworzy obiekt z nowym taskiem i kolejnym id w kolejce
            
            tasks.append(new_task) #dodaje taska do listy tasks zeby dalo sie ladnie odwolac (id w tasku to index w liscie)
            
            print(f"Pomyślnie dodano task (id: {new_task.id})")
        
        else:
            print("Brak drugiego cudzysłowa")


def updating(task_input, tasks):
    print("chuj")