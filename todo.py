import datetime

tasks = []

class Task:
    def __init__(self,id,desc):
        self.id = id
        self.desc = desc
        self.status = "todo"
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()




while True:
    task = input(">>> ")

    # sprawdza tekst w koemndzie ktora wpisujemy
    if task.startswith("add "): #jezeli zaczyna sie z add
        #wyciagamy srodek cudzyslowia
        if "\"" in task: # \" - cudzyslow w pythonie ziomek
            first_quote = task.find("\"") # pierwszego cudzyslowia szuka
            second_quote = task.rfind("\"") # ostatniego cudzyslowia szuka
            if first_quote < second_quote:
                task_desc = task[first_quote+1: second_quote] # wrzuca do zmiennej task_descr to co jest pomiedzy cudzyslowami (dajemy +1 zeby nie zaczelo od cudzyslowia)
                new_task = Task(len(tasks), task_desc) # tworzy obiekt z nowym taskiem i kolejnym id w kolejce
                tasks.append(new_task) #dodaje taska do listy tasks zeby dalo sie ladnie odwolac (id w tasku to index w liscie)
            else:
                print("Brak drugiego cudzysłowa")

    if task == "quit":
        break