# магические и статические методы

# __init__

class Test:

    # Class_Name()
    def __init__(self, value):
        self.value = value

    # print()
    def __str__(self):
        return f'{self.value}'
    
    # +
    def __add__(self, other):
        print(self.value)
        print(other.value)

    # -
    # def __sub__(self, other):

    # *
    # def __mul__(self, other):

    # /
    # def __truediv__(self, other):

    # ==
    # def __eq__(self, value):


    def __getitem__(self, item):
        print(item)


obj_1 = Test(12)
obj_2 = Test(21)

# my_sum = obj_1 + obj_2


class Money:

    def __init__(self, value, currency):
        self.value = value
        self.currency = currency
    
    def __add__(self, other):
        return self.value + other.value
        

tran_1 = Money(5, "USD")
tran_2 = Money(250, "SOM")

# if usd.currency != "SOM":
    # convert_to_som


