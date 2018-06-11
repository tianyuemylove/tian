class tool(object):
    def sushu(self):
        for i in range(100,201):
            flag = True
            for x in range(2,i):
                if i%x == 0:
                    flag = False
                    break
        if flag:
            print(i)
t = tool()
t.sushu()
