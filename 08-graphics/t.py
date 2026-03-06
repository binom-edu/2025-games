class Pet():
    def __init__(self):
        self.name = 'bob'
        self.hp = 100
        self.fuel = 100
    
    def eat(self):
        print('Ням ням')
        self.fuel = min(100, self.fuel + 20)
        print('Заправка:', self.fuel)

class Dog(Pet):
    def __init__(self):
        Pet.__init__(self)

    def say(self):
        print('Гав гав')

class Cat(Pet):
    def __init__(self):
        Pet.__init__(self)

    def say(self):
        print('Мяу')

barsik = Cat()
barsik.name = 'Барсик'
barsik.say()
print(barsik.name)