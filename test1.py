import numpy
from polynomial import *

def test():
    modf = [1,1,0,0,0,0,1]
    g = m_Polynomial([0,1], modf, 2)
    gg = g.powerf(9)
    glist = [g.powerf(9), g.powerf(9*2), g.powerf(9*4)]
    for each in glist:
        print(each.f2s())

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
        b = m_Polynomial(each, modf, p)
        blist = []
        for i in range(6):
            blist.append(b.powerf(p**i))
        table = []
        for each in blist:
            table.append(each.data() + [0 for i in range(len(modf)-1-len(each.data()))])
        if numpy.linalg.matrix_rank(table) == len(modf)-1:
            break
    # calculate base vector
    result = [b]
    for power in range(len(modf)-2):
        b = b.powerf(p)
        result.append(b)
    return result


def basic_test():
    #test Polynomial
    test1 = Polynomial([1,1], 2)
    test2 = Polynomial([1,1,1], 2)
    test3 = Polynomial()
    test4 = Polynomial()
    test3 = test1 * test2
    test4 = test1.modf(test2)
    print("mul: ",test3.data)
    print("mod: ", test4.data)
    print("required False: ", test1==test2)
    test2 = Polynomial([1,1], 2)
    print("required True: ", test1==test2)
    print(test1.f2s())

    #test m_Polynomial
    mtest1 = m_Polynomial([1,1],[1,1,1], 2)
    mtest2 = m_Polynomial([0,1],[1,1,1], 2) 
    mtest3 = mtest1+mtest2
    print(mtest3.f2s())
    mtest3 = mtest1*mtest2
    print(mtest3.f2s())
    print(mtest1.powerf(3).f2s())



if __name__ == '__main__':
    bases = base([1,1,0,0,0,0,1], 2)
    print("64元域正规基们")
    for i in bases:
        print(i.f2s())
    print()
    print("8元子域生成元们")
    test()
