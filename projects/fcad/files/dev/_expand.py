def _expand(a,b):
    h=[]
    k=0
    bb=iter(b)
    while len(h)<len(a):
        try:
            d=next(bb)
        except StopIteration:
            print('iterator stopped')
            bb=iter(b)
        k+=d
        h.append(k)
    return h
