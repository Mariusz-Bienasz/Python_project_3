from functools import reduce
# ########################## Task 1
# Utwórz listę złożoną z pojedynczych liter swojego imienia następnie korzystając
# z funkcji lambda połącz kolejne litery w jeden wyraz (swoje imie)

from Sil import result

# var_string_name = ['M','a','r','i','u','s','z']
#
# result = lambda x: "".join(x)
#
# print(result(var_string_name))

# ########################## Task  2
# Przypisz do zmiennej wartość która będzie twoim imieniem i nazwiskiem następnie korzystając
# z funkcji lambda rozdziel wyraz na poszczegolne wyrazy, a potem wyrazy na litery
# użyj funkcji list i metody split - dla zmiennych typu string

# var_string_name = 'Mariusz Bienasz'
# result = lambda x: x.split()
# var_string_name = result(var_string_name)
# print(var_string_name)
# result = lambda  x: list(x)
#
# for i in var_string_name:
#     print(result(i))

# ########################## Task 3
# # Utwórz funkcję która w dowolnym wyrazie (1 argument funkcji)
# # znajdzie dowolną literę (2 argument funkcji)
## użyj lammbda()

# result = lambda x, y: True if y in x else False
# print(result("Adam", 'd'))

# ########################## Task 4
## Utwórz dwie listy, do każdej z nich niezależnie zapisuj odpowiednio
## podawane przez użytkowników login (pierwsza lista) i hasło (druga lista),
## operacja zapisu jest powtarzana aż do momentu wpisania przez użytkownika "STOP"
## użyj break, continue, enumerate().
## Następnie login-y i hasła zapisz do słownika (login to klucz słownika).
#
# list1 = []
# list2 = []
#
# while True:
#     login = input("Podaj login: ")
#
#     if login == "STOP":
#         break
#
#     password = input("Podaj Hasło: ")
#
#     if password == "STOP":
#         break
#
#     if login == "" or password == "":
#         continue
#
#
#     list1.append(login)
#     list2.append(password)
#
# x = {}
#
# for i,j in enumerate(list1):
#     x[j] = list2[i]
#
# print(x)

# ########################## Task 5  - Module in Python
# # # Zmodyfikuj poprzednie zadanie, tworząc a następnie importując moduł
# # #Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # #Utwórz funkcje Pion: która rysuje gwiazdki pionowo, liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # obie funkcje są z modułu o nazwie stars
# # Korzystając z modułu stars i funkcji Pion Poziom wypisz litery: E, L

# import Task4
# import Stars
#
# Stars.poziom(5)
# Stars.pion(1)
# Stars.poziom(5)
# Stars.pion(1)
# Stars.poziom(5)
# print("\n")
# Stars.pion(4)
# Stars.poziom(5)

# ########################## Task 6
# # utwórz moduł o nazwie sil, w którym znajdzie się funkcja silnia (użyj lammbda), a następnie korzystając z
# modułu sil, oblicz symbol Newtona dla dowolnych 2 liczb wskazanych przez
# użytkownika(http://www.fizykon.org/wzory/wzory_matem_kombinatoryka.htm)

# import Sil
#
# var_int_x = int(input("Podaj liczbe x: "))
# var_int_y = int(input("Podaj liczbe y: "))
#
# result =  (Sil.result(var_int_x))/(Sil.result(var_int_y) * Sil.result(var_int_x-var_int_y))
#
# print(result)

# ########################## Task 7
# # Write a script to filter out only the even items from a list (i.e. made from range(1, 100))
# # using filter() and lambda functions.
# #  The numbers obtained should be printed in a comma-separated sequence on a single line.

# numbers = range(1,100)
# even_numbers = filter(lambda x: x%2 == 0, numbers)
#
# result = ", ".join(map(str, even_numbers))
#
# print(result)

# ########################## Task 8
#### Write a script, using reduce(), which will multiply elements in range (1, 100)

# numbers = range(1,100)
#
# result = reduce(lambda x,y: x*y, numbers)
#
# print(result)

# ########################## Task 9
### Write a program which will find all such numbers which are
### divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included)
### use filter

# def f(x):
#     return x % 7 == 0 and x % 5 != 0
#
# numbers = range(2000,3201)
#
# filtered = filter(f,numbers)
# print(list(filtered))

# ########################## Task 10
### Write a program which will find all such numbers which are
### divisible by 7 but are not a multiple of 5 between 2000 and 3200 (both included)
### use lambda, filter

# numbers = range(2000,3201)
#
# filtered = filter(lambda x: x%7 == 0 and  x%5 != 0, numbers)
#
# print(list(filtered))


# ########################## Task 11
#  # # Utwórz funkcje Poziom: która rysuje gwiazdki poziomo, liczbę gwiazdek podaje użytkownik
##### jako argument funkcji
# # # Utwórz funkcje Pion: która rysuje gwiazdki pionowo,
# ### liczbę gwiazdek podaje użytkownik jako argument funkcji')
# # # Korzystając z w/w funkcji narysuj litery: E, L
### Użyj lambda, użyj wbudowanych funkcji, skróć maksymalnie kod programu, użytkownik, jako wejściowy argument podaje litere E lub L

# poziom = lambda x: print('*' * x)
# pion = lambda x: print(*['*'] * x, sep='\n')
#
# var_input = input("Podaj litere E lub L: ").upper()
#
# draw = {
#     'E' : lambda: [poziom(5), pion(1), poziom(5), pion(1), poziom(5)],
#     'L' : lambda : [pion(4), poziom(5)]
# }
#
# draw.get(var_input, lambda : print("Error"))()