from abc import ABC, abstractmethod


class Hero(ABC):


    def __init__(self, name, level, health, strength ):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength
    
    
    def greet(self):
        return f'Привет, я {self.name}, мой уровень {self.level}'
    
    def rest(self):
        return f'{self.name} отдыхает'
        self.__health += 1
    
    @abstractmethod
    def attack(self):
        pass
    

class Warrior(Hero):
    def __init__(self, name, level, health, strength):
        super().__init__(name, level, health, strength)

    def attack(self):
        return 'Воин атакует мечом'


class Mage(Hero):

    def attack(self):
        return 'Маг использует магию'


class Assassin(Hero):

    def attack(self):
        return 'Ассасин атакует из-под тишка'
    


warrior = Warrior("Мечник", 8, 10, 100)
mage = Mage("Маг", 5, 4, 120)
assasin = Assassin("Ассасин", 10, 2, 80)


print(warrior.greet())
print(warrior.attack())
print(warrior.rest())

print(mage.greet())
print(mage.attack())
print(mage.rest())

print(assasin.greet())
print(assasin.attack())
print(assasin.rest())