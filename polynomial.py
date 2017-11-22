
def divf(x,g):
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

print(divf([8,4,3,2,0], [4,3,2,1,0]))
