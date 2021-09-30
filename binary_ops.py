import sys

def base_2_to_10(base_2_list):
    x = 0
    for i in range(len(base_2_list))[::-1]:
        y = 2 ** i * base_2_list[-i-1]
        # print(i,base_2_list[i],y)
        x += y
    return x

def cambio_di_base(numb, base=2):
    r_list = []

    x = numb
    while x > 0:
        r = x % base
        q = (x - r)//2
        x = q
        r_list.append(r)

    r_list = r_list[::-1]

    return r_list

# assume m >= n
def append_leading_zeros(m,n):
    dif = len(m) - len(n)
    n = [0 for i in range(dif)] + n
    return n

def binary_sum(x,y):
    if len(x) > len(y):
        m,n = x,y
    else:
        m,n = y,x

    n = append_leading_zeros(m,n)

    sum_list = []
    sum_result = {
    '000':(0,0),
    '010':(1,0),
    '100':(1,0),
    '110':(0,1),
    '001':(1,0),
    '011':(0,1),
    '101':(0,1),
    '111':(1,1),
    }

    j = 0
    carry = 0
    for i in range(len(m))[::-1]:
        bit_sum = str(m[i]) + str(n[i]) + str(carry)
        value, carry = sum_result[bit_sum]
        sum_list.insert(0,value)
        j += 1

    if carry == 1:
        sum_list.insert(0,1)
        j += 1


    return sum_list

def binary_product(x,y):

    if len(x) > len(y):
        m, n = x,y
    else:
        m, n = y,x

    shifts = []
    list_addends = []
    for i in n[::-1]:
        if i == 1:
            list_addends.append(m+shifts)
        shifts.append(0)

    i = len(list_addends)

    partial_sums = list_addends
    while i > 1:
        partial_sums = binary_sum(list_addends[i-1],list_addends[i-2])
        i -= 1

    return shifts, list_addends, partial_sums

def binary_division(m,n):
    pass



#
# m = cambio_di_base(m,2)
# n = cambio_di_base(n,2)
# print(m)
# print(n)
# binary_product(m,n)
# print(m)
# print(append_leading_zeros(m,n))
# print(x)
