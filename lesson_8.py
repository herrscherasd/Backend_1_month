#  Исключения
# def div(num1 : int = 2, num2 : int = 2) -> float:
#     try:    
#         return num1 / num2
#     except ZeroDivisionError:
#         return "Деление на ноль??? Карл ты серьезно?!? Иди во второй класс!!!!"
#     except TypeError:
#         return "Пиши целые числа"
# print(div(10, 5))
# print(div(10, 2))
# print(div(10, 5))
# print(div("10", "0"))

# def calculator():
#     while True:
#         try:
#             num1 = int(input("Введите первое число: "))
#             operator = (input("+, -, *, /: "))
#             num2 = int(input("Введите второе число: "))
#             if operator == "+":
#                 print(num1 + num2)
#             elif operator == "-":
#                 print(num1 - num2)
#             elif operator == "*":
#                 print(num1 * num2)
#             elif operator == "/":
#                 try:
#                     print(num1 / num2)
#                 except ZeroDivisionError:
#                     print("Деление на ноль??? Карл ты серьезно?!? Иди во второй класс!!!!")
#             else:
#                 print("Оператор не найден")
#         except ValueError:
#             print("Введите целые числа")
# calculator()

# try:
#     print(10 / 2)
# except:
#     print("Ошибка")
#     # raise ValueError("Делать нехрен ошибку специально выводим) с помощью raise")
# finally:
#     print("Я буду работать")

# f = open("hello.txt", "w")
# f.write("GeekTech")
# f.close()

# r = open("hello.txt", "r")
# print(r.read())
# r.close()


# print(time.ctime())

# def safe_login_password(login : str, password : str) -> str:
#     password_file = open('login_passwords.txt', "a+")
#     if login and len(password) >= 8 and ' ' not in password:
#         password_file.write(f"{login}, {password}, {time.ctime()}\n")
#     else:
#         return "Неправильный логин или пароль"
#     password_file.close()
#     return "Логин и пароль сохранен"
    
# print(safe_login_password("Archon", "Herrscher"))
# print(safe_login_password("Askhat", "Geekcoin"))
# print(safe_login_password("Nurbolot", "Geekcoin2"))
# print(safe_login_password("anon", "        "))

# with open ('geek.txt', 'a+') as g:
#     g.write("Askhat\n")

# with open ('geek.txt', 'r') as r:
#     print(r.read())

import time
import random
# print(random.randint(1, 100))

def generate_random_number():
    return random.randint(1, 10)

def user_contact(name : str, number : str, secret_key : str):
    with open("wins.txt", "a+", encoding = 'utf-8') as win:
        win.write(f"Имя: {name}, Номер: {number}, Секретный код: {secret_key} Дата: {time.ctime()}\n")

def main():
    random_number = generate_random_number()
    counter = 0
    while True:
        user_input = int(input("Введите число от 1 до 10: "))
        counter += 1
        if random_number == user_input:
            print("Вы выиграли! Введите данные для контакта: ")
            name = input("Введите свое имя: ")
            number = input("Введите свой номер: ")
            secret_key = input("Введите секретное слово для получения приза: ")
            user_contact(name, number, secret_key)
            print("Данные сохранены")
            break
        else:
            print(f"Вы не угадали {5 - counter} попыток")
            if 5 - counter == 0:
                break
main()


print("Geekstudio")