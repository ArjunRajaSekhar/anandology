def unique(x):
    i=0
    d=0
    y=[]
    while(i<len(x)):
         d=0
         f=x[i] in y
         if(f==False):
           y.append(x[i])
         i=i+1
    return y
print (unique(["py","py","qw","ui","qwqwqwqwq","ui","UI"]))
print(unique([1,2,3,1,2,3,4,4,4,5,6,7,8,9,0]))
