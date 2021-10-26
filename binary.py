from binary_ops import *
from binary_ops_signed import *
import math

class Binary:

    def __init__(self, numb=None, sign=None):
        if numb == None:
            self.abs_value = []
            self.sign = None

        elif type(numb) == int:
            self.abs_value = base_10_to_base_2(int(math.fabs(numb)))
            self.sign = 1 if numb >= 0 else -1

        elif type(numb) == list:
            self.abs_value = remove_leading_zeros(numb)
            self.sign = sign

    def base10(self):
        return base_2_to_base_10(self.abs_value)

    # def __str__(self):
    #     return str(self.abs_value)

    def __add__(self,other):
        abs_value_base2, sign_bit  = signed_addition(self.abs_value, other.abs_value, self.sign, other.sign)

        return Binary(abs_value_base2,sign_bit)
    #
    # def __sub__(self,other):
    #     return Binary(signed_subtraction(self.abs_value,other.abs_value))

    def __mul__(self, other):
        abs_value_base2, sign_bit  = signed_multiplication(self.abs_value, other.abs_value, self.sign, other.sign)

        return Binary(abs_value_base2,sign_bit)

    # def __truediv__(self, other):
    #     q,r = binary_division(self.abs_value, other.abs_value)
    #     return Binary(q), Binary(r)
    #
    # def __mod__(self,other):
    #     q,r = binary_division(self.abs_value, other.abs_value)
    #     return Binary(r)
    #
    # def __pow__(self, other):
    #     return Binary(binary_power(self.abs_value, other.abs_value))
    #
    # def __eq__(self,other):
    #     return is_equal(self.abs_value, other.abs_value)
    #
    # def __ge__(self, other):
    #     return is_greater_or_equal(self.abs_value, other.abs_value)
    #
    # def __gt__(self, other):
    #     return is_greater(self.abs_value, other.abs_value)

    @staticmethod
    def gcd(self,other):
        d = extended_eucludian_algorithm(self.abs_value, other.abs_value)
        return Binary(d)

    @staticmethod
    def is_value_power(self)
        pass 


x = Binary(2)
y = Binary(0)
z = x * y

print(z.abs_value)
print(z.sign)



a = Binary(-2)
b = Binary(0)
c = a * b

print(c.abs_value)
print(c.sign)

x1 = Binary(2)
y1 = Binary(-2)
z1 = x1 + y1

print(z1.abs_value)
print(z1.sign)

a1 = Binary(-2)
b1 = Binary(2)
c1 = a1 + b1

print(c1.abs_value)
print(c1.sign)
