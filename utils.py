import json
import os
from classes import Task

FILE = "tasks.json"

def save(tasks):
    data = [task.to_dict() for task in tasks]
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load():
    if not os.path.exists(FILE):
        return []

    with open(FILE, "r", encoding="utf-8") as f:
        raw = json.load(f)

    return [Task.from_dict(item) for item in raw]

#funkcja wyciagajaca slowa spomiedzy cudzyslowiow
def pull_from_quotes(task_input):
        first_quote = task_input.find("\"") # pierwszego cudzyslowia szuka
        second_quote = task_input.rfind("\"") # ostatniego cudzyslowia szuka
        
        if first_quote < second_quote: # sprawdza czy odpowiednio sa zrobione cudzyslowia (sa dwa)
            result = task_input[first_quote+1: second_quote] # wrzuca do zmiennej task_descr to co jest pomiedzy cudzyslowami (dajemy +1 zeby nie zaczelo od cudzyslowia)
            return result
        else:
            print("Brak odpowiednich cudzysłowów")
            return None

#funkcja wyciagajaca indexy
def pull_id(task_index):
    parts = task_index.split() # split() dzieli tekst wedlug spacji na liste slow

    if parts[1].isdigit(): # sprawdza czy w liscie parts jest wiecej nz 2 elementy, a potem czy rzecz na indexie 1 jest liczba
        return int(parts[1]) # oddaje liczbe jako int (znowu to co jest na liscie w indexie 1)
    else:
        print("Brak poprawnego numeru")
        return None
    
#funkcja wyciagajaca status
def pull_status(task_index):
    parts = task_index.split()
    if len(parts) == 1:
        return "samo"
    elif parts[1] == "done" or parts[1] == "todo" or parts[1] == "in-progress":
        return parts[1]
    else:
        return None
