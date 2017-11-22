from ISmath import *
#RSA

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
    while not is_prime(p):
        p = randint(100000, 999999)
    while not is_prime(q):
        q = randint(100000, 999999)
    n = p * q
    pn = (p - 1) * (q - 1)
    while not (is_prime(e) and gcd(e, pn)==1):
        e = randint(5, 500)
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
    tmp = base64.b64encode(num_to_str(tmp).encode('utf-8'))
    print(num_to_str(tmp).encode('utf-8'))
    return tmp

def RSA_decode(code, n, e):
    tmp = str_to_num(base64.b64decode(code).decode('utf-8'))
    for i in range(len(tmp)):
        tmp[i] = encode(tmp[i], n, e)
    return num_to_str(tmp)



def main():
    text = "Mathematical Fundation of Information Security 20170406 515030910484"
    num = [283531804, 6248181726, 35435308102, 9859027277, 20391966540, 11616297425, 31443256477, 8364022397, 38492983187, 46019202204, 24562149223, 35541083970, 18115159332, 29620511898, 21656993606, 40405793584, 38336804895]
    print(text)
    private_key, public_key = generate_key()
    print(private_key, public_key)

    code = RSA_encode(text, public_key[0], public_key[1])
    print(code)
    re_text = RSA_decode(code, private_key[0], private_key[1])
    print(re_text)


if __name__ == '__main__':
    #main()
    pass
