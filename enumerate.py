def enum(x):
    ind=range(len(x))
    t=zip(ind,x)
    return [(a,b) for a,b in t]
for index, value in enum(["a", "b", "c"]):
    print (index,value)
