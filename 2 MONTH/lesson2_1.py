
# ООП

class Hero:

    # конструктор класс
    def __init__(self, name, lvl, hp):
        # Атрибуты класса
        self.name = name
        self.lvl = lvl
        self.hp = hp


# обьект/экземпляр на основе класса
kirito = Hero(name="Kirito", lvl=100, hp=1000)
asuna = Hero(name="Asuna", lvl=101, hp=1001)

print(kirito.name)

