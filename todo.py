import datetime

class Task:
    def __init__(self,desc):
        id = 0
        self.desc = desc
        self.status = "todo"
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()




while True:
    task = input()

    # sprawdza tekst w koemndzie ktora wpisujemy
    if task.startswith("add "): #jezeli zaczyna sie z add
        #wyciagamy srodek cudzyslowia
        if "\"" in task: # \" - cudzyslow w pythonie ziomek
            first_quote = task.find("\"") # pierwszego cudzyslowia szuka
            second_quote = task.rfind("\"") # ostatniego cudzyslowia szuka
            if first_quote > second_quote:
                task_desc = task[first_quote+1, second_quote] # wrzuca do zmiennej task_descr to co jest pomiedzy cudzyslowami (dajemy +1 zeby nie zaczelo od cudzyslowia)
                

            else:
                print("Brak drugiego cudzysłowa")
