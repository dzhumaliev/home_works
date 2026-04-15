

# списки

objects_list = [12, 6.3, 45.12, 56, 0.5, 5.5]
# print(objects_list)

# name = ["ISAK"]

# print(name[0][0])
# print(name[0][1])
# print(name[0][2])
# print(name[0][3])


# срезы [start:stop:step]  (stop +1 всегда)

# print(objects_list[2:5:1])
# print(objects_list[2:5])
# print(objects_list[:3])

# print(objects_list[::])
# print(objects_list[::2])
# print(objects_list[::-1])

# print(objects_list[2][:2])


# add 
# objects_list.append(999)
# print(objects_list)
# objects_list.insert(0, 11)
# objects_list.extend([44, 55, 66])
# objects_list += [77, 88]


# print(objects_list)

# edit

# objects_list.sort()
# objects_list.sort(reverse=True)
# objects_list.reverse()

# objects_list[1], objects_list[-1] = objects_list[-1], objects_list[1]
# objects_list[0] = 33

# objects_list[-2::] = [23, 34]

# from random import shuffle

# shuffle(objects_list)


# objects_list.remove(56)
# delete = objects_list.pop(0)
# del objects_list[-2:]
# objects_list.clear
# print(delete)

# print(len(objects_list))
# print(all(objects_list))
# print(any(objects_list))
# print(min(objects_list))
# print(max(objects_list))
# print(sum(objects_list))


# List Comprehension
"""обьект - цикл - условие"""

print(objects_list)

# objects_list2 = [number for number in objects_list if isinstance(number, int)]
objects_list2 = [number * 0.2 for number in objects_list if type(number) == float]



# кортежи не изменяются (tuple)


# numbers = 1, 2, 3, 4, 5
# numbers = (1, 2, 3, 4, 5)
# number = 23,
# print(numbers)



print(objects_list2)

