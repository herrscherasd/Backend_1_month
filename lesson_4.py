#Множества set, frozenset
# numbers = {1, 2, 3, 4, 5, 6, 7, 8, 8, 9}
# print(numbers)
# # print(numbers[0]) #Нельзя вывести в set по индексу
# print(numbers[::1])# Set не поддерживает срезы

# names = {"Askhat", "Kurmanbek", "Daniel", "Asylbek"}
# print(names)
# names.add("Nursultan") # добавляет Нурсултан в set множество
# print(names)
# names.remove("Askhat") # Удаляет Ashkat из множества
# print(names)
# names.pop() # Удаляет случайный элемент из множества
# print(names)
# # names.update("Kurmanbek") # Добавил Kurmanbek и разделил по буквам
# # print(names)
# names.clear() # Очищает множество set
# print(names)

# list = []
# print(type(list))
# hello = ""
# print(type(hello))
# st = {}
# print(type(st))

# list = [10, 4.0, False, "Geek", [1, 2, 3], {1, 2, 3, 3}]
# print(list)
# st = {1, 1.0 , "1", True} #В set нельзя хранить set и list
# print(st)
# sft = {1, 1.1, False, "1"}
# print(sft)
# frzn = frozenset([1, 2, 3, 4, 5, 6])
# print(frzn)
# frzn.add(10)
# print(frzn)

#Tuple - Кортеж. Считвй как список только его нельзя изменить. Или преобзаровать его в лист изменить и обратно
# numbers = (1, 2, 10, 20, 4, 3)
# print(type(numbers))
# tup = (1, 1.0, True, "hELLO", [1, 2, 3], {1, 2, 2}, (10, 20))
# print(tup)
# print(tup.count(1))
# print(tup.index(1))
# print(tup[2])
# print(tup[0:3])'

# cars = ("BMW", "Toyota", "Ferrari")
# print(cars)
# lst_cars = list(cars)
# print(lst_cars)
# lst_cars.append("Tesla")
# print(lst_cars)
# cars = tuple(lst_cars)
# print(cars)

# tup = (10,)# Нужно ставить один элемент только с запятой иначе это не тупл
# print(tup)

student = {"student" : "Askhat", "age" : 18}# сначала обратится к словарю потом к ключу и будет значение
print(student)
print(len(student))# Вывод длины словаря student по элементам "ключ-значение"
print(student["age"])# Вывод значенич с помощью ключа
student.setdefault('language', 'Python')# Добавление нового ключа
print(student)
student.pop("age")# Удаление по ключу
print(student)
student["language"] = "Javascript" # Обновление инфы через ключ
print(student)
student["place"] = "GeekTech" # Добавление еще один способ
print(student)
print(student.keys())# Вывод ключей из словаря
print(student.values())# Вывод значений из словаря
student.setdefault("student1", "Askhat")
print(student)

contact = {'Askhat' : '0778909091'}
while True:
    command = input("1 - получить все контакты, 2 - добавить контакт, 3 - удалить контакт, 4 - обновить контакт: ")
    if command == "1":
        print(contact)
    elif command == "2":
        add_name = input("Введите имя: ")
        add_number = input("Введите номер: ")
        if add_name not in contact:
            contact.setdefault(add_name, add_number)
            print("Контакт успешно добавлен.")
        else:
            print("Контакт уже добавлен.")
    elif command == "3":
        delete_name = input("Введите имя контакта которого удаляете: ").title
        if delete_name in contact:
            contact.pop(delete_name)
            print("Контакт успешно удален.")
        else:
            print("Такого контакта нет.")
    
    elif command == "4":
        updat_comtact = input("Введите имя контакта которого хотите обновить: ")
        number_updat = input("Введите номер контакта: ")
        contact[updat_comtact] = number_updat
        print("Контакт обновлен.")
    else:
        print("Ошибка")