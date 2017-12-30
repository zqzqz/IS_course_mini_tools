class Polynomial(object):
    def __init__(self, value=[], p=2):
        """
            value: list
            p: int
            e.g. [1,1,0,1] means x^3+x+1
        """
        for i in value:
            if i<0 or i>p-1:
                raise ValueError('coefficients of polynomial out of range')
        if len(value)>0 and value[-1]!=1:
            raise ValueError('first term of polynomial should not be zero')
        self.data = value
        if p<2:
            raise ValueError('invalid mod number')
        self.mod = p

    def __add__(self, obj):
        if self.mod != obj.mod:
            raise ValueError('Polynomial with different mod to add')
        index = 0
        result = []
        while index<len(self.data) and index<len(obj.data):
            result.append((self.data[index] + obj.data[index])%self.mod)
            index += 1
        while index<len(self.data):
            result.append(self.data[index])
            index += 1
        while index<len(obj.data):
            result.append(obj.data[index])
            index += 1
        # formalize the polynomial: delete head zeros
        while len(result)>0 and result[-1]==0:
            result.pop()
        
        return Polynomial(result, self.mod)

    def __radd__(self, obj):
        return self + obj

    def __mul__(self, obj):
        if self.mod != obj.mod:
            raise ValueError('Polynomial with different mod to mul')
        result = Polynomial([], self.mod)
        for muli in range(len(self.data)):
            if self.data[muli]==0:
                continue
            tmp_result = [0 for i in range(muli)]
            for mulj in range(len(obj.data)):
                tmp_result.append((obj.data[mulj]*self.data[muli])%self.mod)
            # call custom add operator
            result = result + Polynomial(tmp_result, self.mod)
        return result
    
    def __rmul__(self, obj):
        return self * obj

    def __eq__(self, obj):
        if self.mod != obj.mod:
            raise ValueError('Polynomial with different mod')
        return (self.data == obj.data)
        
    def __ne__(self, obj):
        if self.mod != obj.mod:
            raise ValueError('Polynomial with different mod')
        return (self.data != obj.data)
    
    def modf(self, obj):
        """
            obj: Polynomial
            calculate: self mod(obj)
        """
        if self.mod != obj.mod:
            raise ValueError('Polynomial with different mod to mod')
        result = self
        while len(result.data) >= len(obj.data):
            result = result + Polynomial([0 for i in range(len(result.data)-len(obj.data))] + obj.data, self.mod)
        return result

    def f2s(self):
        """
            return string format data
        """
        if len(self.data)==0:
            return "0"
        result = ""
        for i in range(len(self.data)-1,-1,-1):
            if self.data[i] == 0:
                continue
            if i != len(self.data)-1:
                result += " + "
            if self.data[i] != 1 or i==0:
                result += str(self.data[i])
            elif i > 1:
                result += "x^" + str(i)
            elif i ==1:
                result += "x"
        return result

class m_Polynomial(object):
    def __init__(self, obj, modf, p=2):
        """
            obj: list[int]
            modf: list[int]
            p: int
        """
        if len(obj) >= len(modf):
            raise ValueError("obj's length should be shorter than modf")
        self.obj = Polynomial(obj, p)
        self.modf = Polynomial(modf, p)
        self.mod = p

    def data(self):
        return self.obj.data

    def f2s(self):
        return self.obj.f2s()

    def __add__(self, other):
        if self.modf != other.modf:
            raise ValueError("different mod polynomial")
        return m_Polynomial((self.obj+other.obj).modf(self.modf).data, self.modf.data, self.mod)
    
    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if self.modf != other.modf:
            raise ValueError("different mod polynomial")
        return m_Polynomial((self.obj*other.obj).modf(self.modf).data, self.modf.data, self.mod)
    
    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if self.modf != other.modf:
            raise ValueError("different mod polynomial")
        return self.obj == other.obj

    def __ne__(self, other):
        if self.modf != other.modf:
            raise ValueError("different mod polynomial")
        return self.obj != other.obj

    def powerf(self, n):
        if n<0:
            raise ValueError("the power number should not be negative")
        elif n==0:
            return self
        result = Polynomial([1], self.mod)
        tmp_pow = self.obj
        index = 0
        while n>>index: 
            if (n>>index)%2:
                result = (result * tmp_pow).modf(self.modf)
            tmp_pow = (tmp_pow * tmp_pow).modf(self.modf)
            index += 1;
        return m_Polynomial(result.data, self.modf.data, self.mod)

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


