# Словари (dict) и множества

# {key: value}


# print(set('google'))


# beshbarmak = {"мясо", "тесто", "лук"}
# plov = {"морковь", "рис", "мясо"}

# print(beshbarmak.union(plov))
# print(beshbarmak | plov)


# print(beshbarmak.intersection(plov))
# print(beshbarmak & plov)


# print(beshbarmak.difference(plov))
# print(beshbarmak - plov)


# print(beshbarmak.symmetric_difference(plov))
# print(beshbarmak ^ plov)


# numbers1 = [1, 2, 3, 4, 5, 2, 4, 1, 3]
# numbers2 = {1, 2, 3, 4, 5, 2, 4, 1, 3}

# print(numbers1)
# print(numbers2)

# print(type(numbers2))



# student = {
#     'name': 'Isak',
#     "age": 27
# }
# edit 
# student['age'] = 20
# student['name'] = 'ISAK'

# add 
# student['country'] = 'kg'
# student.update({'height': 183, 'weight': 80})


# delete
# student.pop('age')
# del student['name']


# print(student)
# print(student['name'])
# print(student.get('surname', 'нет такого ключа!'))



# print(student.items())

# вывод пар ключ значений
# for key, value in student.items():
#     print(f'{key}: {value}')



# for i in student:
#     print(i, student[i])


# product_list = ['apple', 'milk', 'water']
# product_dic = {'apple': 20, 'milk': 15, 'water': 30}

