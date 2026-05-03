

# Расходы на продукты в неделю

monday = int(input("Введите расходы на продукты в понедельник: "))
tuesday = int(input("Введите расходы на продукты во вторник: "))
wednesday = int(input("Введите расходы на продукты в среду: "))
thursday = int(input("Введите расходы на продукты в четверг: "))
friday = int(input("Введите расходы на продукты в пятницу: "))

print("")
print("Результат:")

total = monday + tuesday + wednesday + thursday + friday
print("Всего было потрачено за неделю на расходы:", total)

average = total / 5

print("Средняя сумма расходов на продукты в день:", average)


if average >= 1 and average <= 100:
    print("Малый расход")
elif average >= 101 and average <= 400:
    print ("Средний расход")
elif average >= 401:
    print("Высокий расход")
else:
    print("Ничего не потрачено")