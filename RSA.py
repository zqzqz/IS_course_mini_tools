#! usr/bin/python #coding=utf-8
#python 3.x
from math import *
from random import *
import base64
#RSA demo
#明文分组：32bits
#大素数p,q范围(1000000,10000000)
#字符数字化规则 ascii-hex


prime_list=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
            97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191,
            193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
            307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419,
            421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541,
            547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
            659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
            797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919,
            929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
#1000以内质数表


def gcd(a,b):  #欧几里得除法，辗转相除求最大公约数
    while b != 0:
        a,b = b,a%b
    return a


def jacobi(a,n):
    if n%2==0:
        return
    result = 1
    nf = -1
    af = -1
    while a!=1:   #互反律计算
        while a&1!=1:
            a = a>>1
            if ((n * n - 1) >> 3) & 1 == 0:
                result *= 1
            else:
                result *= (-1)
        if a==1:
            break
        if nf == -1:
            nf = ((n-1)>>1)&1
        else:
            nf = af
        af = ((a - 1) >> 1) & 1
        if ((a-1)>>1)&1==1 and ((n-1)>>1)&1==1:
            result *= (-1)
        a,n = n%a , a
    if a==1:
        result *= 1
    return result


def is_prime(x):
    if x%2==0:
        return 0
    if x>1000000:                     #对于大素数使用Solovay-Stassen素数检验
        for k in range(1000):
            b = randint(2,x-2)
            r = quick_mod(b, (x-1)>>1 , x)
            if r!=1 and r!=(x-1):
                return 0
            if r==(x-1):
                r = -1
            if jacobi(b,x)!=r:
                return 0
        return 1
    for i in prime_list:
        if x%i == 0:
            return 0
        if i > sqrt(x):
            return 1
    return 1


def reverse(a,b):   #广义欧几里得除法求逆元
    tmp = b
    if gcd(a,b)!=1:
        return 0
    s1=1
    s2=0
    t1=0
    t2=1
    while b%a!=0:
        r = b//a
        b, a = a, b%a
        tmp1 = s1 - r * s2
        tmp2 = t1 - r * t2
        s1, s2 = s2, tmp1
        t1, t2 = t2, tmp2
    while t2<0:
        t2 += tmp
    return t2

def divide(n):
    list=[]
    m=2
    while n!=1:
        while n%m==0:
            list.append(m)
            n = n//m
        m+=1
    return list



def quick_mod(a, b, m):  #快速模运算 a^b modm
    list = []
    i = 0
    if a>m:
        a = a%m
    while (b>>i) > 0:
        list.append((b>>i) & 1)
        i+=1
    #print(list)
    result = 1
    tmp = a % m
    for i in range(len(list)):
        if i!=0:
            tmp = (tmp * tmp) % m
        if list[i]:
            result = (result * tmp * list[i]) % m
    return result



def str_to_num(str):
    asc=[]
    for i in range(len(str)):
        asc.append(ord(str[i]))
    for j in range(4-len(str)%4):
        asc.append(0)
    flag = 0
    result = []
    while flag < len(str):
        tmp = 0
        for f in range(4):
            t = asc.pop(0)
            tmp = tmp*16*16 + t
        result.append(tmp)
        flag += 4
    return result

def num_to_str(num):
    result = ""
    for sub in num:
        tmp = ""
        tnum = sub
        for i in range(4):
            tmp = str(chr(tnum%(16*16))) + tmp
            tnum = tnum // (16*16)
        result += tmp
    return result

def generate_key():
    p=q=e=4
    p = 2* randint(50000, 500000) +1
    q = 2* randint(50000, 500000) +1
    while not is_prime(p):
        p += 2
    while not is_prime(q):
        q += 2
    n = p * q
    print(p,q)
    pn = (p - 1) * (q - 1)
    while not (is_prime(e) and gcd(e, pn)==1):
        e = randint(6, 500)
    d = reverse(e, pn)

    return (n, e), (n, d)



def encode(text, n, d):
    return quick_mod(text, d, n)

def decode(code, n, e):
    return quick_mod(code, e, n)

def RSA_encode(text, n, d):
    tmp = str_to_num(text)
    for i in range(len(tmp)):
        tmp[i] = encode(tmp[i], n, d)
    #tmp = base64.b64encode(num_to_str(tmp).encode('utf-8'))
    #print(num_to_str(tmp).encode('utf-8'))
    return tmp

def RSA_decode(code, n, e):
    #tmp = str_to_num(base64.b64decode(code).decode('utf-8'))
    tmp = code
    for i in range(len(tmp)):
        tmp[i] = encode(tmp[i], n, e)
    return num_to_str(tmp)



def main():
    text = "Mathematical Fundation of Information Security 20170406 515030910484"
    print('plain text: ',text)
    private_key, public_key = generate_key()
    print('private key: ',private_key,'\npublic key: ', public_key)

    code = RSA_encode(text, public_key[0], public_key[1])
    print('ciphertext in number: ',code)
    print('ciphertext base64: ',base64.b64encode(num_to_str(code).encode('utf-8')).decode('utf-8'))
    re_text = RSA_decode(code, private_key[0], private_key[1])
    print('plain text2: ',re_text)


if __name__ == '__main__':
    main()
