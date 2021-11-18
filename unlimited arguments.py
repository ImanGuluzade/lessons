def a(*arg):
    if sum(arg)>100:
        print("loop end\t",arg)
    else:
        arg=list(map(lambda a: a+1,arg))
        print('in loop:\t',arg)
        return a(*arg)
a(10,20,30)