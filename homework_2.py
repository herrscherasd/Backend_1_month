# #Задание 1
print("Задание №1")# сделал для удобства в терминале тебе)
login = "Archon"
user_login = input("Enter the Login:")
user_password = input("Enter the password: ")
password = "Raiden"
if password == user_password and user_login == login:
    print('Password is correct. You are welcome')
else:
    print('Password is incorrect. Please, try again')

# #Задание 2
print("Задание №2")
user_temp = int(input("Введите температуру за окном: "))
if user_temp < -30:
    print("Там так холодно, лучше дома сиди!")
elif user_temp >= 30 and user_temp < 0:
    print("Холодновато. Оденься потеплее!")
elif user_temp >= 0 and user_temp < 15:
    print("Прохладно. Куртку накинь!")
elif user_temp >= 15 and user_temp < 30:
    print("Тепло. Иди погуляй в парке!")
elif user_temp >= 30 and user_temp <= 50:
    print("Ого, как жарко!")
elif user_temp > 50:
    print("Там такая жара, лучше сиди дома!")
else:
    print("Ошибка!")

# #Задание 3
print("Задание №3")
text = """Advertising companies say advertising is necessary and important. It informs people about
new products. Advertising hoardings in the street make our environment colourful. And
adverts on TV are often funny. Sometimes they are mini-dramas and we wait for the next
programme in the mini-drama. Advertising can educate, too. Adverts tell us about new,
healthy products. And adverts in magazines give us ideas for how to look prettier, be
fashionable and be successful. Without advertising, life is boring and colourless.
But some consumers argue that advertising is a bad thing. They say that advertising is bad
for children. Adverts make children 'pester' their parents buy things for them. Advertisers
know we love our children and want to give them everything. So they use children's 'pester
power' to sell their products. Finally, consumers say, if there is advertising there must be
rules. Some adverts advertise unhealthy things like cigarettes and make people waste their
money."""
print("Букв s в тексте:", text.count("s"))
print("Букв t в тексте:", text.count("t"))

#Доп.задание
print("Доп.задание")
name_1 = "Aidana"
name_2 = "Adilet"
print(name_1[0] + name_2[0] + name_1[1] + name_2[1] + name_1[2] + name_2[2] + name_1[3] + name_2[3] + name_1[4] + name_2[4] + name_1[5] + name_2[5])