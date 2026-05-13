
rates = {
   "KGS": 1,
   "USD": 89,
   "EUR": 96,
   "RUB": 1.2
}

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
        
    def __str__(self):
        return f'{self.amount} {self.currency}'
    
    def convert_to_kgs(self):
        return self.amount * rates[self.currency]
    
    def __add__(self, other):
        return self.convert_to_kgs() + other.convert_to_kgs()
    
    def __sub__(self, other):
        return self.convert_to_kgs() - other.convert_to_kgs()
    
    def __mul__(self, number):
        return f"{self.amount * number} - {self.currency}"
    
    def __truediv__(self, number):
        return f'{self.amount / number} - {self.currency}'


money1 = Money(100, "USD")
money2 = Money(5000, "KGS")

print(money1)
print(money2)

print(money1.convert_to_kgs())
print(money2.convert_to_kgs())

result = money1 - money2

mul_result = money1 * 3
div_result = money2 / 2

# print(result)
print(mul_result)
print(div_result)