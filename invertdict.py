def invertdict(x):
    dic={}
    dic={v: k for k, v in x.items()}
    return dic
print(invertdict({'x': 1, 'y': 2, 'z': 3}))
