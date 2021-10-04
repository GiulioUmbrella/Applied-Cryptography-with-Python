from random import randint

def set_longer_shorter(x,y):
    if len(x) >= len(y):
        return x,y
    else:
        return y,x

def base_2_to_10(base_2_list):
    x = 0
    for i in range(len(base_2_list))[::-1]:
        y = 2 ** i * base_2_list[-i-1]
        # print(i,base_2_list[i],y)
        x += y
    return x

def base_10_to_base_n(numb, base=2):
    r_list = []

    x = numb
    while x > 0:
        r = x % base
        q = (x - r)//2
        x = q
        r_list.append(r)

    r_list = r_list[::-1]

    return r_list

def append_leading_zeros(m,n):
    dif = len(m) - len(n)
    n = [0 for i in range(dif)] + n
    return n

def remove_leading_zeros(n):
    j = 0
    while(j < len(n)-1 and n[j] == 0):
        j += 1
    return n[j:]


def is_greater_or_equal(m,n):
    if len(m) > len(n):
        return True
    elif len(n) > len(m):
        return False
    else:
        i = 0
        while( m[i] == n[i] ):
            i += 1
            if i == len(m):
                break
        if i == len(m):
            return True
        elif m[i] > n[i]:
            return True
        else:
            return False

def is_greater(m,n):
    if len(m) > len(n):
        return True
    elif len(n) > len(m):
        return False
    else:
        i = 0
        while i < len(m) and m[i] == n[i]:
            i += 1
        if i == len(m):
            return False
        else:
            return m[i] > n[i]



def binary_addition(x,y):
    m,n = set_longer_shorter(x,y)
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

    # ops = 0
    carry = 0
    for i in range(len(m))[::-1]:
        bit_sum = str(m[i]) + str(n[i]) + str(carry)
        # bit_key = ''.join(map(str, [m[i],n[i],carry]))
        value, carry = sum_result[bit_sum]
        sum_list.insert(0,value)
        # ops += 1

    if carry == 1:
        sum_list.insert(0,1)
        # ops += 1


    return sum_list

def binary_product(x,y):
    m,n = set_longer_shorter(x,y)

    # ops = 0
    shifts = []
    list_addends = []
    for i in n[::-1]:
        # ops += 1
        if i == 1:
            list_addends.append(m+shifts)
        shifts.append(0)

    i = 1
    partial_sums = list_addends[0]

    while i < len(list_addends):
        # x, partial_sums = binary_addition(partial_sums,list_addends[i])
        partial_sums = binary_addition(partial_sums,list_addends[i])
        # ops += x
        i += 1

    return partial_sums
    # return ops, list_addends, partial_sums

def binary_subtraction(x,y):
    # m,n = set_longer_shorter(x,y)
    m = x
    n = append_leading_zeros(x,y)

    result_list = []
    i = len(m)-1
    sub_res = {'00':0,'10':1,'11':0}

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

    return remove_leading_zeros(result_list)

def binary_division(m,n):

    q = []
    r = []
    j,i = 0,1
    while(i < len(m)+1): # ?

        if is_greater(n,r + m[j:i]):
            q.append(0)
        else:
            # print(j,i)
            # print('q', q)
            # print('r', r)
            # print('m[j:i]', m[j:i])
            # print('r + m[j:i]',r + m[j:i])
            q.append(1)
            r = binary_subtraction(r + m[j:i], n)
            # r = binary_subtraction(r, n)
            j = i
        i += 1

    return q,r


def sequence_product():
    pass
# num_values = 10
# max_value  = 10
# list_values = [base_10_to_base_n(randint(1, max_value)) for i in range(num_values)]
#
# partial_product = list_values[0]
# for i in range(1,len(list_values)):
#     partial_product = binary_product(partial_product, list_values[i])
#
# print(partial_product)

def sequence_product_modular():
    pass
