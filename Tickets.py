tickets = int(input("Укажите количество билетов, которое хотите приобрести на мероприятие:"))
age = list(map(int,input("Укажите возраст посетителей: ").split()))
while tickets != len(age):
    age = list(map(int, input("Количество посетителей не совпадает с количеством билетов.\n"
                              "Укажите возраст посетитилей:").split()))
price = []
for i in age:
    if i in range(0,18):
        price.append(0)
    elif i in range(18,25):
        price.append(990)
    else:
        price.append(1390)
if tickets > 3:
    print("Сумма с учетом скидки:", sum(price)-((sum(price)/100)*10),"рублей")
else:
    print("Сумма к оплате:", sum(price), "рублей")