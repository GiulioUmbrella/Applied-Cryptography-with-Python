from binary_ops import *
# import binary_ops

class Binary:

    def __init__(self, numb=None):
        if numb == None:
            self.value = []
        elif type(numb) == int:
            self.value = base_10_to_base_2(numb)
        elif type(numb) == list:
            self.value = remove_leading_zeros(numb)

    def base10(self):
        return base_2_to_base_10(self.value)

    def __str__(self):
        return str(self.value)

    def __add__(self,other):
        return Binary(binary_addition(self.value, other.value))

    def __sub__(self,other):
        return Binary(binary_subtraction(self.value,other.value))

    def __mul__(self, other):
        return Binary(binary_product(self.value,other.value))

    def __truediv__(self, other):
        q,r = binary_division(self.value, other.value)
        return Binary(q), Binary(r)

    def __mod__(self,other):
        q,r = binary_division(self.value, other.value)
        return Binary(r)

    def __pow__(self, other):
        return Binary(binary_power(self.value, other.value))

    def __eq__(self,other):
        return is_equal(self.value, other.value)

    def __ge__(self, other):
        return is_greater_or_equal(self.value, other.value)

    def __gt__(self, other):
        return is_greater(self.value, other.value)

    @staticmethod
    def gcd(self,other):
        d = extended_eucludian_algorithm(self.value, other.value)
        return Binary(d)


x = Binary(16324)
y = Binary(782)
d = Binary.gcd(x,y).base10()
print(d)
