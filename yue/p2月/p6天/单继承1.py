class People:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.tui = 10
        self.weiba = 9
    def eat(self):
        print('%s正在吃炸鸡' % self.name)
        print('*'* 9)
        print('%s正在喝啤酒' % self.name)
        print('%s是头猪' % self.name)
class ren(People):
    def jiao(self):
        print('正在叫————')
hua=ren('王一凡',9,'女')
hua.eat()
print('%s'+str(hua.tui) + 条腿)
