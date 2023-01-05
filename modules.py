#импортировать сам модуль
# import lesson_7

# print(lesson_7.get_time())
# print(lesson_7.hello())
#Импортировать отдельное определение из модуля
# from lesson_7 import get_time, hello
# print(get_time())
# print(hello())

#импортировать все содержимое модуля сразу
# from lesson_7 import * # * импортирует всё
# print(get_time())
# print(hello())
# print(it)

###########################################
from lesson_7 import numbers, chert

def chert_nechert(num : list) -> list:
    for i in num:

        if i % 2 == 0:
            chert.append(i)
    return chert
# print(chert_nechert(numbers))
