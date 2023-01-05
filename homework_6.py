#Задание 1 
# def abbreviatura():
#     word = input("Введите слово: ").split()
#     for i in word:
#         print(i[0].title(), end = "")
# abbreviatura()

#Задание 2
# def counter():
#     phrase = input("Введите фразу: ").lower().split()
#     for d in phrase:
#         print(d, "=", phrase.count(d))
# counter()

#Задание 3
# def isogram():
#     word = input("Введите изограмму: ")
#     if len(word) == len(set(word)):
#         print("True")
#     else:
#         print("False")
# isogram()

#Задание 4
# def revers(n : int):
#     n2 = 0
#     while n > 0:
#         # находим остаток - последнюю цифру
#         digit = n % 10
#         # делим нацело - удаляем последнюю цифру
#         n = n // 10
#         # увеличиваем разрядность второго числа
#         n2 = n2 * 10
#         # добавляем очередную цифру
#         n2 = n2 + digit  
#     print(n2)
# revers(1042)

#Доп.задание 5
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
# chat_bot()