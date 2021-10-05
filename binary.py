class Binary:

    def __init__(self, numb=None):
        if numb == None:
            self.value = []
        else:
            r_list = []

            x = numb
            while x > 0:
                r = x % 2
                q = (x - r)//2
                x = q
                r_list.append(r)

            r_list = r_list[::-1]
            self.value = r_list

    def __str__(self):
        return str(self.value)

    @staticmethod
    def set_longer_shorter(x,y):
        if len(x) >= len(y):
            return x,y
        else:
            return y,x

    @staticmethod
    def append_leading_zeros(m,n):
        dif = len(m) - len(n)
        n = [0 for i in range(dif)] + n
        return n


    @staticmethod
    def remove_leading_zero(m):
        pass

    @staticmethood
    def base10_to_base2(m):
        pass

    def base10():
        pass

    def __add__(self,other):
        m,n = Binary.set_longer_shorter(self.value,other.value)
        n = Binary.append_leading_zeros(m,n)

        sum_list = []
        three_bits_sum = {
        '000':(0,0),'010':(1,0),'100':(1,0),'110':(0,1),
        '001':(1,0),'011':(0,1),'101':(0,1),'111':(1,1),
        }

        carry = 0
        for i in range(len(m))[::-1]:
            bit_sum = str(m[i]) + str(n[i]) + str(carry)
            value, carry = three_bits_sum[bit_sum]
            sum_list.insert(0,value)

        if carry == 1:
            sum_list.insert(0,1)

        y = Binary()
        y.value = sum_list
        return y


    def __sub__(self,other):
        m,n = Binary.set_longer_shorter(self.value,other.value)
        n = Binary.append_leading_zeros(m,n)

        sub_res = {'00':0,'10':1,'11':0}
        result_list = []
        i = len(m)-1


        while i > -1:
            bit_pair = str(m[i]) + str(n[i])

            if bit_pair in sub_res:
                result_list.insert(0,sub_res[bit_pair])
            else:
                result_list.insert(0, 1)
                i -= 1
                while( -1 + m[i] - n[i] < 0):
                    result_list.insert(0, 1 + m[i] - n[i])
                    i -= 1
                result_list.insert(0, 0)
            i -= 1

        x = Binary()
        x.value = result_list
        return x


    def __mul__(self, other):
        m,n = Binary.set_longer_shorter(self.value,other.value)

        shifts = []
        list_addends = []
        for i in n[::-1]:
            if i == 1:
                x = Binary()
                x.value = m+shifts
                list_addends.append(x)
            shifts.append(0)

        i = 1
        partial_sums = list_addends[0]

        while i < len(list_addends):
            partial_sums = partial_sums + list_addends[i]
            i += 1

        return partial_sums

    def __eq__(self,other):
        m = self.value
        n = other.value

        if len(m) != len(n):
            return False
        else:
            i = 0
            while i < len(m) and m[i] == n[i]:
                i += 1
        return i == len(m)

    def __ge__(self, other):
        m = self.value
        n = other.value

        if len(n) > len(m):
            return False
        elif len(m) > len(n):
            return True
        else:
            i = 0
            while i < len(m) and m[i] == n[i]:
                i += 1
            if i == len(m):
                return True
            else:
                return m[i] > n[i]


    def __gt__(self, other):
        m = self.value
        n = other.value

        if len(n) > len(m):
            return False
        elif len(m) > len(n):
            return True
        else:
            i = 0
            while i < len(m) and m[i] == n[i]:
                i += 1
            if i == len(m):
                return False
            else:
                return m[i] > n[i]

# x = Binary(10)
# y = Binary(2)
# z = x - y
# print(type(x))
# print(type(y))
# print(type(z))
# print(x)
# print(y)
# print(z)


x = Binary(1)
y = Binary(11)
print(x > y)
