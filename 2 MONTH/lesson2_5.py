



# Decorator

# def simple_decorator(func):
#     def wrapper():
#         print('До выполнения!')
#         func()
#         print('После выполнения!')
#     return wrapper

# @simple_decorator
# def say_hello():
#     print('Hello!')

# # say_hello()

# ------------------------

# def greeting_decorator(func):
#     def wrapper(name):
#         print(f'{name} Привет!')
#         func(name)
#     return wrapper

# @greeting_decorator
# def greet(name):
#     print(f'{name} как дела?')

# greet('Isak')

# ---------------------------

# def repeat_decorator(n):
#     def decorator(func):
#         def wrapper():
#             for i in range(n):
#                 func()
#         return wrapper
#     return decorator

# @repeat_decorator(5)
# def hi():
#     print("Hi!")

# hi()

# -------------------------------

def class_decorator(cls):
    class NewClass(cls):
        def action(self):
            print("New Action!")
    return NewClass

@class_decorator
class OldClass:
    def action(self):
        print("Old Action!")

test_obj = OldClass()
test_obj.action()