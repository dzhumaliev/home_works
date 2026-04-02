

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

print("Средняя сумма расходов на продукты в день:", total / 5)