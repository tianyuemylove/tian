import sys
class People:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
class Worlder:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
hua = People('花花',9000)
hua1 = hua
hua02 = hua
hua03 = hua
print(sys.getrefcount(hua))   # 对象被引用了多少次，数量显示要比实际引用次数 多1
print(isinstance(hua03,Worlder))   # 查询对象是否属于 指定的类


