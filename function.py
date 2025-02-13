import random

def random_element_exclude(lst,exc):
    filtrata = []  
    for el in lst:  
        if el != exc:
            filtrata.append(el)
    elemento = random.choice(lst)  # Seleziona un elemento a caso
    lst.drop(lst[lst == elemento].index, inplace=True)  # Rimuove l'elemento dalla lista
    return elemento