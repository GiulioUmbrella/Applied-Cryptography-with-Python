class Binary:

    def __init__(self, numb=None):
        if numb == None:
            self.value = []
        elif type(numb) == int:
            print(1)
            self.value = Binary.base10_to_base2(numb)
        elif type(numb) == list:
            # remove leading zeros
            self.value = Binary.remove_leading_zero(numb)

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
        j = 0
        while(j < len(m)-1 and m[j] == 0):
            j += 1
        return m[j:]

    @staticmethod
    def base10_to_base2(m):
        r_list = []
        # x = q*2 + r
        # q = x//2
        # r = x -2*(x//2)
        x = m
        while x > 0:
            r = x % 2
            q = (x - r)//2
            x = q
            r_list.append(r)

        return r_list[::-1]


    def base10(self):
        x = 0
        for i in range(len(self.value))[::-1]:
            x += 2 ** i * self.value[-i-1]
        return x

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

        return Binary(sum_list)


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

        # return a binary object
        return Binary(result_list)


    def __mul__(self, other):
        m,n = Binary.set_longer_shorter(self.value,other.value)

        shifts = []
        list_addends = [] # substitute with a Binary object with zero
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


    # Divisione euclidea

    # mod

    # power

    # right shift

    # left shift


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
