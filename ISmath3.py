from ISmath import *
global prime_list

def sim_remain(p):
    result=[]
    for d in range(1, p):
        if gcd(d,p)==1:
            result.append(d)
    return result

def primaryRoot(p):
    if not is_prime(p):
        return False
    n = p-1
    tmp=[]
    result=[]
    for i in range(2, n):
        if n==1:
            break
        while n%i==0:
            n = n//i
            if (len(tmp)==0 or tmp[-1]!=i):
                tmp.append(i)
    for i in range(len(tmp)):
        tmp[i] = (p-1)//tmp[i]
    #-----
    g = 1
    while 1:
        g += 1
        flag=1
        for obj in tmp:
            #print("(%d ^ %d) = %d"%(g,obj,quick_mod(g,obj,p)))
            if quick_mod(g,obj,p)==1:
                flag=0
        if flag:
            break
    #------
    #print("g: ",g)
    d_list = sim_remain(p-1)
    #print(len(d_list))
    for j in d_list:
        result.append(quick_mod(g,j,p))
    return g, result

def primaryRootpa(p, a):
    if not is_prime(p) or a<=0:
        return False
    g = primaryRoot(p)
    #print(g)
    if a==1:
        return g
    tmp = quick_mod(g, p-1, p*p)
    result=-1
    if tmp%p==1:
        result = g
        #print(result)
    tmp = quick_mod(g+p, p-1, p*p)
    if tmp%p==1 and result<0:
        result = g+p
        #print(result)
    #print()

    return result

def createIndTable(p):
    if not is_prime(p) or p<=2:
        return False
    g = primaryRoot(p)
    t = p-1
    dict={}
    tmp = 1
    for i in range(p-1):
        dict[tmp]=t
        tmp = (g*tmp)%p
        t = (t+1)%(p-1)
    return dict

def quick_mul_mod(a,b,m):
    if not is_prime(m) or m<=2:
        return False
    dict = createIndTable(m)
    tmp = dict[a%m]+dict[b%m]
    for key, value in dict.items():
        if value==tmp%m:
            return key
    return

k = quick_mod(43,96,383)
print(k)
print((k*k)%383)
