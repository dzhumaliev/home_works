
# Функции: виды параметров, возвращение данных, виды аргументов


"""из чего состоит функция?"""

#    определение название(параметры):
#        тело функции
#        возвращение результата

#    вызов функции
#    название (аргументы)


# def some_name(name, surname = 'test'):
#     print(f"hello world and {name} and {surname}")


# some_name('isak', "surname")



def get_square(lenght: int, width: int) -> int:
    """ test text for checking doc"""
    return lenght * width



print(get_square.__doc__)
print(help(get_square))
print(get_square(lenght=200, width=150))