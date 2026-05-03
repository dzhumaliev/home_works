
# Домашнее задание 1

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')


    def attack(self):
        self.health -= 1
        print(f'{self.name} наносит удар!')

    def rest(self):
        self.health += 1
        print(f'{self.name} отдыхает…')
    


popovich = Hero(name="Алеша Попович", level=1, health=100, strength=18)

muromec = Hero(name="Илья Муромец", level=1, health=100, strength=22)


popovich.greet()
popovich.attack()
print(f'Уровень здоровья уменьшилось и стало {popovich.health}')
popovich.rest()
print(f'Уровень здоровья восстановилось и стало {popovich.health}')

print('----------------------')

muromec.greet()
muromec.attack()
print(f'Уровень здоровья уменьшилось и стало {muromec.health}')
muromec.rest()
print(f'Уровень здоровья восстановилось и стало {muromec.health}')