class Father(object):
    def __init__(self,name):
        self.name = name
    def kaiche(self):
        print('赛车手*****')
    def eat(self):
        print('吃吃吃****')
class Son(Father):
    def __init__(self,name):
       # self.name = name
        super().__init__(name)
    def kaiche(self):
        print('王一凡垃圾')
        super().kaiche()


putao = Son('葡萄')
putao.eat()
putao.kaiche()
