import arxiv

from _expand import _expand
def _get_val(text,comp,key):
    r=0
    ind=0
    k=_expand(comp,key)
    for i in comp:
        if text[k[ind]]==i:
            r+=1
        ind+=1
    return r
        
def encrypt(text,stre,key):
    if not 0<stre<100:
        raise ValueError('strenght must be in range 0>strenght<100')
    m=arxiv.randompages()
    a=0
    maxi=0
    maxim=None
    for i in m:
        t=arxiv.extract_text(i)
        if _get_val(t,text,key)>=maxi:
            maxim=t
            maxi=_get_val(t,text,key)
        print(f'page has value {_get_val(t,text,key)}')
        a+=1 
        if a==stre:
            break
    kakikak=0
    maximu=list(maxim)
    for i in _expand(text,key):
        maximu[i]=text[kakikak]
        kakikak+=1
    maxim=''.join(maximu)
    return maxim
