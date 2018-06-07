class Student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        self.chengji = {}
    def cj(self,k,v):
        k = input('请输入学科:')
        v = input('请输入成绩:')
        self.chengji[k]  = v
hua = Student('小花',19,'女')
tian = Student('甜甜',17,'女')
ming = Student('小明',21,'男')
hua.cj('语文',190)
print(hua.cj())



















tian = Student('小甜',9,'女',90)

