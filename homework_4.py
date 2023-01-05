#Задание 1
# it_company = ('Google', 'Amazon', 'Microsoft') 
# it_comp = list(it_company)
# it_comp.append('Tesla')
# it_company = tuple(it_comp)
# print(it_company)

#Задание 2
# print(it_company.index('Amazon'))

#Задание 3
# it_comp = list(it_company)
# it_comp[0] = 'Apple'
# it_company = tuple(it_comp)
# print(it_company)

#Задание 4
# print(it_company[0:3])

#Задание 5
# text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
# 'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean',
# 'syntax', 'and', 'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite',
# 'with', 'our', 'python', '3', 'overview')
# print(text_tuple.count("python"))
# counter = 0
# if 'Python' in text_tuple:
#     counter += 1
# if 'python' in text_tuple:
#     counter += 1
# print(counter)

#Задание 6
# dictionary_1 = {'a': 300, 'b': 400} 
# dictionary_2 = {'c': 500, 'd': 600}
# dictionary_1.update(dictionary_2)
# print(dictionary_1)

#Задание 7
# numbers = {'num_1' : 1, 'num_2' : 2,'num_3' : 3, 'num_100' : 100}
# print(numbers['num_1'] * 5, numbers['num_2'] * 5, numbers['num_3'] * 5, numbers['num_100'] * 5)

#Задание 8
# student = {'name' : 'Askhat', 'age' : 17}
# print(student['age'] * 2)

#Задание 9
# student = {'name' : 'Askhat', 'age' : 17, 'color' : 'White'}
# student['age'] = 16
# print(student['age'])

#Задание 10
# student = {'name' : 'Askhat', 'age' : 17}
# student.pop('age')
# print(student)

#Задание 11
# student = {'name' : 'Askhat'}
# student.setdefault("address", "Западный Анар")
# print(student)

#Доп.задание 12
# while True:
#     new_password = input("Введите новый пароль: ")
#     if len(new_password) < 8:
#         print("Короткий пароль")
#     elif "123" in new_password:
#         print("Простой пароль")
#     else:
#         break

# while True:
#     check_password = input("Введите пароль еще раз: ")
#     if new_password !=check_password:
#         print("Различаются!")
#     else:
#         print("OK", "Пароль создан!")
#         break

# Доп.задание 13
contact = {'Askhat' : '0778909091'}
while True:
    command = input("1 - получить все контакты, 2 - добавить контакт, 3 - удалить контакт, 4 - обновить контакт, 5 - Закончить действия: ")
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
        delete_contact = input("Кого хотите удалить: ")
        if delete_contact in contact:
            contact.pop(delete_contact)
            print("Контакт успешно удален.")
        else:
            print("Такого контакта нет.")
    elif command == "4":
        updat_contact = input("Введите имя контакта которого хотите обновить: ")
        if updat_contact in contact:
            number_updat = input("Введите номер контакта: ")
            contact[updat_contact] = number_updat
            print("Контакт обновлен.")
        else:
            print("Контакт не найден.")
    elif command == "5":
        break
    else:
        print("Ошибка")