class  Animal:
    def __init__(self,name,salary):
        self.name = name
        self.salary= salary
        f = opebjn('t.txt','r+')
    def set_name(self):
        return self.name
    def get_name(self):
        self.name = self.f.read()
        if len(self.name) != 0:
            print(self.name)

        else:
            print('文件里面没有内容')
    def __str__(self):
        return '名字:%s,工资:%d' % (self.name,self.salary)
    def __del__(self):
        self.f.write(self.name)
        self.f.color()
        print('------对象已经被销毁-------')
hua = Animal('花猫',100)
print(hua.get_name())
print(hua.set_name())

print('++++')
