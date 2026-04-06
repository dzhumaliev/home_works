
def redColor(text: str):
    return print(f'\033[31m{text} \033[0m')

def greenColor(text: str):
    return print(f'\033[32m{text} \033[0m')

def yellowColor(text: str):
    return print(f'\033[33m{text} \033[0m')

try:
    day =  int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))

    if day < 1 or day > 31 or month > 12 or month < 1:
        redColor("Не правильно введенная дата")
    elif day > 28 and month == 2:
        redColor("Не правильно введенная дата")
    elif (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
        redColor("Не правильно введенная дата") 
        
    elif day >= 21 and month == 3 or day <= 20 and month == 4 :
        greenColor("Овен")
    elif day >= 21 and month == 4 or day <= 21 and month == 5:
        greenColor("Телец")
    elif day >= 22 and month == 5 or day <= 21 and month == 6:
        greenColor("Близнецы")
    elif day >= 22 and month == 6 or day <= 22 and month == 7:
        greenColor("Рак")
    elif day >= 23 and month == 7 or day <= 21 and month == 8:
        greenColor("Лев")
    elif day >= 22 and month == 8 or day <= 23 and month == 9:
        greenColor("Дева")
    elif day >= 24 and month == 9 or day <= 23 and month == 10:
        greenColor("Весы")
    elif day >= 24 and month == 10 or day <= 22 and month == 11:
        greenColor("Скорпион")
    elif day >= 23 and month == 11 or day <= 22 and month == 12:
        greenColor("Стрелец")
    elif day >= 23 and month == 12 or day <= 20 and month == 1:
        greenColor("Козерог")
    elif day >= 21 and month == 1 or day <= 19 and month == 2:
        greenColor("Водолей")
    elif day >= 20 and month == 2 or day <= 20 and month == 3:
        greenColor("Рыбы")
    else:
        redColor("Ошибка, проверьте корректность введенной даты рождения")

except:
    redColor("Введите корректные данные как на примере ниже: ")
    yellowColor("Введите день рождения: 10")
    yellowColor("Введите месяц рождения: 12")
  



