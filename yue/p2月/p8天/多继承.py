class Donkey(object):
    def manzou(self):
        print('喜欢吃炸鸡')
    def jiao(self):
        print('喜欢小熊熊')
class Horse(object):
    def nai(self):
        print('喜欢跑步')
    def jiao(self):
        print('喜欢兔兔')
class Mule(Donkey,Horse):
    print('*' * 9)
ai = Mule()
ai.manzou()
ai.nai()
ai.jiao()
print(Mule.__mro__)
