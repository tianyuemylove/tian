class People(object):
    guoji = 'china'
    def __init__(self):
        self.name = '花花'
    def get_name(self):
        return self.name
    @classmethod
    def get_guoji(cls):
        return cls.guoji
    @classmethod
    def say_chinese(cls):
        print('生活中国画')
    @staticmethod
    def get_name()
        print('')
print(People.guoji)
hua = People()
hua.guoji = 'ss'
print(hua.guoji)
del hua.guoji
print(hua.guoji)
