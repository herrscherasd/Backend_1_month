#Задание 5
# def square(x : int, y : int):
#     return x * y

# def perimeter(x : int, y : int):
#     return x + y

#Задание 6
lst = [1, 2, 3, 4 ,5, 6, 7, 8, 9, 10]
def revers(y : list) -> list:
    return y[::-1]

#Задание 7
# hours, minutes, seconds = int(input("Введите кол-во часов: ")), int(input("Введите кол-во минут: ")), int(input("Введите кол-во секунд: "))
# def converter(x : int, y : int, z : int):
#     return (x * 3600) + (y * 60) + z
    
#Задание 8
# def chat_bot():
#     while True:
#         word = input("Введите сообщение: ")
#         if len(word) > 2 and "?" in word:
#             print("Конечно!")
#         elif word == word.upper() and len(word) > 1:
#             print("Успокойся")
#         elif "" in word and len(word) == 0:
#             print("Как классно, когда ты молчишь. Продолжай в том же духе")
#         else:
#             print("Ну и что")

#Задание 9
# def abbreviatura():
#     word = input("Введите слово: ").split()
#     for i in word:
#         print(i[0].title(), end = "")

#Доп.Задание 10
menu = {'beefstrogonoff' : 350,'burger' : 200,'meatloaf' : 500,'chicken pot pie' : 400,'beefshteks' : 650}
def new_menu(lst : list):
    newmenu = {x : y + 50 for x, y in lst.items()}
    return newmenu