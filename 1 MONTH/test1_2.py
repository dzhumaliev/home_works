

# Конвертация текста

eng_layout = "qwertyuiop[]asdfghjkl;'zxcvbnm,./ "
rus_layout = "йцукенгшщзхъфывапролджэячсмитьбю. "

layout_map = dict(zip(eng_layout + rus_layout, rus_layout + eng_layout))

while True:
    word = input("Введите слово: для выхода нажмите 'q' ").lower()
 

    if word == 'q':
        print("программа завершена")
        break
    
    result = ""
    for char in word:
        result += layout_map.get(char, char)
        
    print(result)




# Вычисление скидки


def my_discount(points_map):
    total = points_map['home_work'] + points_map['test']

    if total >= 300:
        return 3000
    elif total >= 200:
        return 2000
    elif total >= 100:
        return 1000
    return 0


points_map = {
    "home_work": 0,
    "test": 0,
    "attendance": 0
}

while True:
    points_hw = input('Введите балл за дз: ')
    if points_hw.lower() == 'exit':
        break

    points_test = input('Введите балл за контрольную: ')
    if points_test.lower() == 'exit':
        break


    points_map['home_work'] += int(points_hw)
    points_map['test'] += int(points_test)

    print(f"Ваша скидка составляет: {my_discount(points_map)}")
