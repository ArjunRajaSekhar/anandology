def sum(x):
    i=1
    while(i<len(x)):
         x[i]=x[i-1]+x[i]
         i=i+1
    return x[i-1]
print (sum(["abc","def","qwe","rty"]))
print (sum([2,4,3,5]))
