

def sim_continued_fraction(p,q):
    a = []
    x = (q,p)
    pm2 = qm1 = 0
    qm2 = pm1 = 1
    while x[0]!=0:
        tmp_a = x[1]//x[0]
        x = (x[1]-tmp_a*x[0],x[0])
        pm1, pm2 = tmp_a*pm1+pm2, pm1
        qm1, qm2 = tmp_a * qm1 + qm2, qm1
        print(tmp_a,x,(pm1,qm1))
        a.append(tmp_a)
    return a

list=[208.09,610.28,757.87,810.43,828.48,832.86,843.39,862.82,862.50,865.35,
      841.75,832.44,808.26,750.99,609.68,400.88,119.07]
for i in list:
    print(i, i/6.999)

#print(1/(1/10+1/39.8))
def solve():
    x = 1000
    tmp = 0
    tmp1 = 1000
    c = 0
    while 1:
        c += 1
        y = 1/x + 1/10 + 1/39.8
        y = 1/y
        print(x,y,tmp)
        if c>30:
            pass
        if abs(y-2.278)<0.0001:
            return x
        if y<2.278:
            tmp = x
            x= (x + tmp1)/2
        elif y>2.278:
            tmp1 = x
            x = x/2
        else:
            return x

