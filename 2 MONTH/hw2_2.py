# 📝 Домашнее задание №2

# Тема: Наследование и полиморфизм в ООП
# 📌 Задание
# Создайте родительский класс Hero, такой же как в прошлом домашнем задании.

# Атрибуты класса Hero
# name — имя героя
# level — уровень героя
# health — здоровье
# strength — сила

# Методы класса
# greet() — выводит приветствие
# attack() — герой наносит удар
# rest() — герой отдыхает и восстанавливает здоровье

# 📌 Создать дочерние классы
# От класса Hero должны наследоваться:
 
# Warrior (Воин)
# Mage (Маг)
# Assassin (Ассасин)

# 📌 Дополнить конструктор дочерних классов
# Каждый дочерний класс должен иметь свой дополнительный атрибут.

# Warrior
# добавить атрибут
# stamina — выносливость

# Mage
# добавить атрибут
# mana — мана 

# Assassin
# добавить атрибут
# stealth — скрытность 

# 📌 Переопределить метод attack()
# Каждый класс должен по-своему реализовать метод атаки.
# Warrior
# Воин атакует мечом! 

# Mage
# Маг кастует заклинание!

# Assassin
# Ассасин атакует из-под тишка!

# Это и есть пример полиморфизма.


# 📌 Создать объекты
# Создать по одному объекту каждого класса:

# один Warrior
# один Mage
# один Assassin

# 🎮 Мини-игра "Камень, Ножницы, Бумага"

# Реализовать игровую логику:
# Соответствие героев:

# Warrior  = Камень
# Assassin = Ножницы
# Mage     = Бумага

# Логика игры

# 1️⃣ При запуске программы спросить пользователя:
# Выберите героя:
# Warrior / Mage / Assassin

# 2️⃣ После выбора пользователя:
# программа случайно выбирает противника из созданных объектов 

# 3️⃣ Определяется победитель по правилам:
# Воин побеждает Ассасина
# Ассасин побеждает Мага
# Маг побеждает Воина 

# 4️⃣ Вывести результат боя:
# Пример:
# Вы выбрали: Warrior
# Противник: Mage

# Mage победил! 

# 📦 Что нужно сдать

# 1️⃣ Python файл с решением
# 2️⃣ Залить код на GitHub
# 3️⃣ Отправить ссылку на репозиторий


import random

class Hero:
    def __init__(self, name, lvl, hp, strg):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.strg = strg
    
    
    def greet(self):
        print(f'Приветствую {self.name}!')
    
    def attack(self):
        print(f'{self.name} наносит удар!')
    
    def rest(self):
        print(f'{self.name} отдыхает и восстанавливает здоровье!')
    

class Warrior(Hero):
    def __init__(self, name, lvl, hp, strg, stamina):
        super().__init__(name, lvl, hp, strg)
        self.stamina = stamina
  
    def attack(self):
        print(f"{self.name} атакует мечом!")

class Mage(Hero):
    def __init__(self, name, lvl, hp, strg, mana):
        super().__init__(name, lvl, hp, strg)
        self.mana = mana
    
    def attack(self):
        print(f"{self.name} кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, lvl, hp, strg, stealth):
        super().__init__(name, lvl, hp, strg)
        self.stealth = stealth
    
    def attack(self):
        print(f"{self.name} атакует из-под тишка!")


wr = Warrior(name="Воин", lvl=100, hp=10, strg=100, stamina=10)
mg = Mage(name="Маг", lvl=1000, hp=100, strg=100, mana=10)
asn = Assassin(name="Ассасин", lvl=1000, hp=100, strg=100, stealth=10)

wr.attack()
mg.attack()
asn.attack()

hero_dict = {"Warrior": wr, "Mage": mg, "Assassin": asn}

new_hero = input('Выберите героя:\n Warrior / Mage / Assassin ')

random_choice = random.choice(["Warrior", "Mage", "Assassin"])

wins_dict = {"Warrior": "Assassin",
        "Assassin": "Mage",
        "Mage": "Warrior" }

if new_hero not in hero_dict:
    print('Введите корректного героя!')
else:
    player = hero_dict[new_hero]

    enemy = hero_dict[random_choice]

    print(f'Вы выбрали: {player.name}')
    print(f'Противник: {enemy.name}')

    if new_hero == random_choice:
        print("Ничья!")
    elif wins_dict[new_hero] == random_choice:
        print(f"{hero_dict[new_hero].name} победил!")
    else:
        print("Вы проиграли!")
    
