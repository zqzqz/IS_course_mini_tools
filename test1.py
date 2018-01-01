from polynomial_util import *

def test():
    modf = [1,1,0,0,0,0,1]
    g = m_Polynomial([0,1], modf, 2)
    gg = g.powerf(9)
    glist = [g.powerf(9), g.powerf(9*2), g.powerf(9*4)]
    for each in glist:
        print(each.f2s())


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
    modf = [1,1,0,0,0,0,1]
    g = m_Polynomial([0,1],modf,2)
    print(is_g(g))
    glist = [g.powerf(9), g.powerf(9*2), g.powerf(9*4)]
    for each in glist:
        print(each.f2s())
    print("index:")
    print("1")
    print((glist[0]+glist[1]+glist[2]).f2s())
    print((glist[0]*glist[1]+glist[0]*glist[2]+glist[1]*glist[2]).f2s())
    print((glist[0]*glist[1]*glist[2]).f2s())
    print()
    print("bases")
    blist = base(modf, 2)
    for each in blist:
        print(each.f2s())
    print()
    gg = g.powerf(9)
    print('0')
    for i in range(1,8):
        print(gg.powerf(i).f2s())
    print()
    for i in range(8):
        g = m_Polynomial([],modf,2)
        if i%2:
            g = g + glist[0]
        if (i>>1)%2:
            g = g + glist[1]
        if (i>>2)%2:
            g = g + glist[2]
        print(g.f2s())
