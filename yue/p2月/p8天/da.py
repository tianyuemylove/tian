class Father(object):
    def __init__(self):
        self.name = '啦啦'
        self.__height = '155'
    def eat(self):
        print('吃吃吃')
        print('睡睡睡‘’‘')
    def __dobo(self):
        print('赌博。。。。。。')
class Son(Father):
    print('*' * 9)
hua = Son()
hua.name = '慕容'
print(hua.name)
hua.height = '190'
hua.eat()
print(hua.height)

