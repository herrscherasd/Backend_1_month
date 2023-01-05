#Циклы for и while.  for нужен чтобы пройтись по каждому элементу списка или чего то еще
# for i in range(2, 1001, 2):
#     print(i)

# names = ["Kurmanbek", "Daniel", "Askhat", "Nursultan"]
# for d in names:
#     # print(d)
#     if d == "Askhat":
#         print("Askhat есть.")
# ..
# numbers = [1, 10, 112, 13, 231, 23323, 1111]
# for i in numbers:
#     if i % 2 == 0:
#         print(i, "чет")
#     else:
#         print(i, "нечет")

# name = "Kurmanbek"
# for n in name:
#     if n == "a":
#         print("Буква есть")
    # print(n)

# number = "100" #int bool и float не итерируется
# for num in number:
#     print(num)

# cities_tuр = ("Osh", "Bishkek", "Talas", "Tokmok")
# for city in cities_tuр:
#     print(city)

# cars = {"BMW", "Mercedes", "Tesla", "Honda"}
# for car in cars:
#     print(car)

# student = {"name" : "Daniel", "age" : "18", "language" : "Python"}
# for key, values in student.items():
#     # print(key, values)
#     if key == "language" and values == "Python":
#         print("Питонист найден.")

# numbers = []
# for i in range(1,1001):
#     numbers.append(i)
# print(numbers)

# for i in range(1, 11):
#     print(i)
#     if i == 6:
#         print("STOP")
#         continue

# numbers = [10, 20, 30, 40, 50]
# for i, n in enumerate(numbers):# итерирует элементы указывая индекс тоже
#     print(i, n)

# num1 = 10
# num2 = 20
# while num1 < num2:
#     print(num1)
#     num1 += 1 #развернуто += это num1 = num1 + 1
    
# import random

# n = 0
# random_number = random.randint(1, 10000)
# print(random_number)
# while True:
#     n += 1
#     print(n)
#     if n == random_number:
#         break

import time

process = 0
while True:
    print(str(process) + "% HACK")
    process += 1
    time.sleep(0.1)
    if process == 100:
        print("SUCCESSFULLY HACKED")
        break

