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
