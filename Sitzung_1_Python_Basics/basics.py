
#%% Typen
hw:str = "hallo welt!" #string (Zeichkette)
print(hw[1]) #Indizierung fängt mit 0 an
hw2:str = hw + "wie gehts?" #+-Zeichen verbindet Strings

# Benennung ohne Anführungszeichen: Numerische Datentypen ODER schon existierende Variablen
a:int = 2 #int
b:float = 3.0 #float
print(a+b)
"""
Mehrzeilen-
kommentare
"""
#Typecasting
c = int(b)
b = "hallo welt"

d = "hallo welt" + str(3)

list_of_ints = [1,2,3]
print(list_of_ints[0])

#Listen müssen nicht typenrein sein!
mixed_list = [1,2,"3",hw]
print(mixed_list)

#dictionary: keyword:value
fruits = {'Apple':5,'Banana':10,'Orange':7}
print(fruits['Apple'])

fruit_prices = {"Apple":{"stock": 5, "price": 2}}
print(fruit_prices["Apple"]["price"])

#set
list1 = [1,2,3]
print(set(list1))


list2 = [2,2,2,3,3,3]
print(set(list2))

print(set(list1)-set(list2))

import numpy as np
arr1 = np.array(list1) #Arrays müssen typenrein sein

2*list1 #hängt die Liste zweimal aneinander
2*arr1 #multipliziert jedes Element mit 2


#%% Loops und Funktionen

list1 = [1,2,3]

# list1[0]*2,list1[1]*2



# for-loop
list1timestwo = []
for n in list1:
    list1timestwo.append(2*n)


print(list1timestwo)

# while-loops

# List comprehensions (Loop auf einer Zeile)

list1_multiplied = [n*2 for n in list1]

print(list1_multiplied)

#%%
# Funktionen können Eingabe- und Ausgabewerte haben
def square(n):
    """
    Parameters
    ----------
    n : number (int or float)

    Returns
    -------
    squared_number : squared number

    """
    squared_number = n*n #Funktionen haben einen lokalen Scope
    return squared_number



list1_squared = [square(n) for n in list1]
print(list1_squared)


# Klassen (class) Objekt, das mehrere Funktionen und / oder Daten und / oder
# Zustände speichern kann


















