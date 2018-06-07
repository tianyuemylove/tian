class Animal:
    def eat(self):
        print('兔兔正在吃炸鸡')
    def drink(self):
        print('兔兔正在喝啤酒')
    def shui(self):
        print('兔兔正在睡觉')
class Dog(Animal):
    def jiao(self):
        print('狗狗正在叫——————————')
l = Dog()
l.eat()
l.drink()
l.shui()
l.jiao()
