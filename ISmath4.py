from ISmath import reverse

def chinese_remain_theroem(list):
    result=0
    M = 1
    for t in range(len(list)):
        M *= list[t][1]
    tmp = M
    for i in range(len(list)):
        b = list[i][0]
        M = M//list[i][1]
        if i!=0:
            M = M*list[i-1][1]
        M1 = reverse(M, list[i][1])
        result += (b*M*M1)
    return result % tmp

if __name__ == '__main__':
    print(chinese_remain_theroem([(2,3),(3,5),(2,7)]))