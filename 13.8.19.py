#Стоимость
cost = 0

#Вывод на экран необходимого количества билетов
ticket = int(input("Введите необходимое количество билетов:"))
L = []
for price in range (1, ticket+1) :
    age = int(input("Введите возраст посетителя:"))
    if 0<= age < 18:
        price = 0
    elif 18 <= age <= 24:
        price = 990
    elif 25<= age <=99:
        price = 1390
    else:
        print("Введите корректный возраст!")
    L.append(price)
if len(L)>3:
    cost =int(sum(L) / 100 * 90)

print('Итого'+ ' ' + str(round(cost)) + ' ' + 'руб.')