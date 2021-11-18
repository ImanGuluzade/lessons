def a(v):
    if v>10:
        print("loop stopped\t",v)
        return v
    else:
        v+=1
        print("in loop:\t",v)
        return a(v)
a(2)