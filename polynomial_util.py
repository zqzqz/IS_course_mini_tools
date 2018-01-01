from polynomial import *
import numpy
from basic_util import *

def base(modf, p):
    """
        modf: list[int]
        p: int
        return: list[m_Polynomial]
    """
    test_list = []
    #build test set
    for i in range(p**(len(modf)-1)):
        num = i
        tmp = []
        while num>0:
            tmp.append(num%p)
            num = num//p
        test_list.append(tmp)
    # find a answer by cycling
    b = m_Polynomial([1],modf,p)
    for each in test_list:
        # calculate base vector
        b = m_Polynomial(each, modf, p)
        if is_base(b):
            break
    result = [b]
    for power in range(len(modf)-2):
        b = b.powerf(p)
        result.append(b)
    return result

def is_base(beta):
    """
        beta: m_Polynomial
    """
    blist = []
    for i in range(6):
        blist.append(beta.powerf(beta.mod**i))
    table = []
    for each in blist:
        table.append(each.data() + [0 for i in range(len(each.modf.data)-1-len(each.data()))])
    if numpy.linalg.matrix_rank(table) == len(each.modf.data)-1:
        return True
    return False


def is_g(g):
    """
        g: m_Polynomial
    """
    m = 2**(len(g.modf.data)-1)-1
    prime_list = []
    for i in range(3,int(sqrt(m)+1)):
        if m%i==0 and is_prime(i):
            prime_list.append(i)
    for prime in prime_list:
        if g.powerf(m//prime).obj.data == [1]:
            return False
    return True


def is_gf(modf, p):
    """
        modf: list[int]
        p: int
    """
    m = 2**(len(modf)-1)-1
    prime_list = []
    g = m_Polynomial([0,1], modf, p)
    for i in range(3,int(sqrt(m)+1)):
        if m%i==0 and is_prime(i):
            prime_list.append(i)
    for prime in prime_list:
        if g.powerf(m//prime).obj.data == [1]:
            return False
    return True


