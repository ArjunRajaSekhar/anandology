def unique(x):
    y=set(x)
    return (list(y))
lower=lambda x:x.lower()
upper=lambda x:x.upper()
def unique1(x,f):
    i=0
    while i<len(x):
         x[i]=f(x[i])
         i=i+1
    return unique(x)
print(unique1(["py","py","qw","ui","qwqwqwqwq","ui","UI"],lower))
