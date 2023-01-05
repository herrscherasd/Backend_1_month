# it = "Geektech" #Индексы
#      #01234567
# print(it[0])
# print(it[4])
# print(it[3])
# print(it[4] + it[5] + it[6] + it[7])
# print(it[0:4]) #До какого то элемента не включая его
# print(it[4:8:2])# Срезы

#List - списки
# cars = [1, "1", True, 19.9]
# print(type(cars))

# name1 = "Kurmanbek"
# name2 = "Askhat"
# name3 = "Daniel"
# print(name1)

# names = ["Kurmanbek", "Askhat", "Daniel"]
# print(names)
# names.append("Asylbek")#Добавление элемента в списокв конец
# print(names)
# names.remove("Kurmanbek")#Удаление по названию
# print(names)
# names.pop(0)#Удаление по индексу
# print(names)
# names.insert(0, "Askhat")#Добавление по индексу
# print(names)
# names[0] = "Asko"#Переназначение элемента списка
# print(names)
# cities = ["Bishkek", "Osh", "Tokmok", "Naryn"]
# print(cities[0:2])
# print(cities[::-1])# Вывод в обратном порядке
# cities.sort()
# print(cities)
# cities.reverse()# Еще обратка
# print(cities)

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# del numbers[0:3:2]
# print(numbers)
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers))
# print(numbers.count(70))
# print(numbers.index(80))#Находит под каким индексом элемент

# contacts = ["Askhat"]
# name = input("Введите имя: ").title()
# if name in contacts:
#     print(name, "найден")
# else:
#     print(name, "не найден")

#Приложение Контакты
contacts = ["Askhat"]
while True:
    command = input("1 - посмотреть контакты, 2 - добавить контакт, 3 - удалить контакт, 4 - обновить контакт: ")
    if command == "1":
        print(contacts)
    elif command == "2":
        add_contact = input("Кого хотите добавить?: ").title()
        if add_contact in contacts:
            print("Контакт уже добавлен:")
        else:
            contacts.append(add_contact)
            print("Удачно добавлен в контакты.")
    elif command == "3":
        delete_contact = input("Кого хотите удалить?: ").title()
        if delete_contact in contacts:
            contacts.remove(delete_contact)
            print("Контакт успешно удален")
        else:
            print("Контакт не найден.")
    elif command == "4":
        update_contact = input("Кого хотите обновить?: ").title()
        if update_contact in contacts:
            new_contact = input("Новое имя: ")
            contacts[contacts.index(update_contact)] = new_contact
            print("Успешно обновлено")
        else:
            print("Контакт не найден.")
            