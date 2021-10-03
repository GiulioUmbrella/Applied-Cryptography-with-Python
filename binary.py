class Binary:

    def __init__(self, numb):
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
        return str(''.join(self.value))

    @staticmethod
    def set_longer_shorter(x,y):
        if len(x) >= len(y):
            return x,y
        else:
            return y,x

    def __add__(self,other):
        m = self.value
        n = other.value

        print(m)
        print(n)

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

        return sum_list

x = Binary(2)
y = Binary(1)
print(x+y)
