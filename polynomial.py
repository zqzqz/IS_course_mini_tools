
def divf2(x,g):
    """
        x: list[int]
        g: list[int]
        return: q: list; r: list
        x = q * g +r
    """
    x.sort(reverse=True)
    g.sort(reverse=True)
    xx = x+[]
    q = []
    while len(xx)>0 and xx[0]>=g[0]:
        q.append(xx[0]-g[0])
        for i in g:
            try:
                index = xx.index(i+q[-1])
                del xx[index]
            except:
                xx.append(i+q[-1])
        xx.sort(reverse=True)
    return q, xx    


def addf2(a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    re = a + []
    for i in b:
        try:
            index = re.index(i)
            del re[index]
        except:
            re.append(i)
    re.sort(reverse=True)
    return re

def multif2(a,b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    re = []
    for i in a:
        for j in b:
            try:
                index = re.index(i+j)
                del re[index]
            except:
                re.append(i+j)
    re.sort(reverse=True)
    

def quick_mod_f(b, f):  #快速模运算 x^b mod(f(x))
    pass



print(
