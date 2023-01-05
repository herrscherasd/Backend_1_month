#Условие if else elif
num1 = 20
num2 = 50
if num1 > num2:
    print(num1)
else:
    print(num2)

number = 30
if number % 2 == 0:
    print(number, 'четное')
else:
    print(number, 'нечетное')
    
name = input("Введите своё имя: ")
print("Здравствуйте", name)

num1 = int(input("Введите первое число:"))
operator = input("+, -, *, /:")
num2 = int(input("Введите второе число:"))
if operator == "+":
    print("Ответ:", num1 + num2)
elif operator == "-":
    print("Ответ:", num1 - num2)
elif operator == "*":
    print("Ответ:", num1 * num2)
elif operator == "/":
    print("Ответ:", num1 / num2)
else:
    print("Введи по человечески!!!!")

#or, and
login = 'geektech'
password = 'geektech2021'
user_login = input("Login:")
user_password = input("Password:")
if login == user_login and user_password == password:
    print("Welcome")
else:
    print("Неверный логин или пароль.")

number = int(input("Number: "))
if number >= 0 and number < 10:
    print("Между 0 и 10")
elif number >= 10 and number < 20:
    print("Между 10 и 20")
elif number >= 20 and number < 30:
    print("Между 20 и 30")
elif number >= 30 and number < 40:
    print("Между 30 и 40")

#', ", """ """
str_example_one = 'Hello. I\'m Geektech student.'# \ чинит проблему с кавычкой '
print(str_example_one)
str_example_two = "Hello. I'm Geektech student.\nI'm studying Python language." #Нельзя писать тексты больше одной строки или большие.или можно переместить текст на новую строку командой \n
print(str_example_two)
str_example_three = """Hello. I'm Geekteech student.
I'm study Python language."""
print(str_example_three)

name = "aSkhAT"
print(name.title())# title делает первую букву заглавной остальные мелкими
print(name.upper())# upper все буквы с большой
print(name.lower())# lower все буквы с маленькой

print(20 == 30)
print(100 == 100.0)

print(20 != 30)
print(3 != 3)

print(20 > 5)
print(40 > 100)

print(5 < 6)
print(40 < 4)

print(30 >= 30)

print(30 <= 50)
