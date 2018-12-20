def reverse(x):
    filehandle=open(x,'r')
    contents=(filehandle.read()).split()
    print(contents)
    reverseoffile=contents[::-1]
    print(reverseoffile)
    reverse=' '.join(str(i) for i in reverseoffile)
    print(reverse)

reverse('sample.txt')



