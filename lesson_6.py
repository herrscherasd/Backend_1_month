# Функции
# def calc():
#     num1 = int(input("Введите первое число: "))
#     num2 = int(input("Введите второе число: "))
#     print(num1 + num2)
# # calc()

# def calc(num1, num2): #Параметры num1, num2
#     print(num1 + num2)
# calc(10, 20) #К параметрам num1, num2 передаются аргументы

# def hello_world():
#     print("Hello World")
# # hello_world()

# def func_while():
#     while True:
#         print("Geektech")
# func_while()

# numbers = [10, 20, 1, 5, 3, 44]
# print(max(numbers))

# def max(arg):
#     print("Geektech")
# print(max(numbers))

# def print(word):
#     pass
# print("Helllo world")

# def hekko_user(name : str) -> str:
#     print("Здравствуйте,", name)
# hekko_user("Asyl")
# hekko_user("Askhat")
# hekko_user("Daniel")
# hekko_user(30)

# def add(num1 : int, num2 : int):
#     print(num1 + num2)

# def sub(num1 : int, num2 : int):
#     print(num1 - num2)

# def mult(num1 : int, num2 : int):
#     print(num1 * num2)

# def div(num1 : int, num2 : int):
#     print(num1 / num2)

# def calculator(num1 : int,  operator: str, num2 : int):
#     if operator == "+":
#         add(num1, num2)
#     elif operator == "-":
#         sub(num1, num2)
#     elif operator == "*":
#         mult(num1, num2)
#     elif operator == "/":
#         div(num1, num2)
#     else:
#         print("Error")
# calculator(30, "+", 60)

# def chet_nechet(num : int = 2) -> str: #два тут это значение по умолчанию
#     if num % 2 == 0:
#         print(num, "четный")
#     else:
#         print(num, "нечетный")
# chet_nechet(222)
# chet_nechet(333)
# chet_nechet()# Если пустой аргумент то применится значение по умолчанию если есть

# numbers = [10, 20, 1, 5, 3, 44]
# tup_numbers = (2, 3, 312, 121, 63, 76, 765)
# def list_chet(lst_num : list) -> str:
#     for num in lst_num:
#         if num % 2 == 0:
#             print(num, "четный")
#         else:
#             print(num, "нечетный")
# list_chet(numbers)
# list_chet(tup_numbers)

def hello():
    return "Hello GeekTech"
print(hello())