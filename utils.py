def pull_from_quotes(task_input):
    while True:
        first_quote = task_input.find("\"") # pierwszego cudzyslowia szuka
        second_quote = task_input.rfind("\"") # ostatniego cudzyslowia szuka
        if first_quote < second_quote:    
            result = task_input[first_quote+1: second_quote] # wrzuca do zmiennej task_descr to co jest pomiedzy cudzyslowami (dajemy +1 zeby nie zaczelo od cudzyslowia)
            return result
        else:
            print("Brak drugiego cudzysłowa")
            task_input = input(">>> ")