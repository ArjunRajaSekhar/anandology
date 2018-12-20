def cenalign(x):
    i=0
    tl=140
    f=open(x).readlines()
    l=len(f)
    print(len(f))
    s=''
    while i<l:
        s=s+ ' '*int((tl-len(f[i]))/2)+f[i].strip()+' '*int((tl-len(f[i]))/2)+'\n'
        i=i+1
    return s
import sys
print(cenalign(sys.argv[1]))
