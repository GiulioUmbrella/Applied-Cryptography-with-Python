def set_longer_shorter(x,y):
    if len(x) >= len(y):
        return x,y
    else:
        return y,x

def base_2_to_base_10(base_2_list):
    x = 0
    for i in range(len(base_2_list))[::-1]:
        y = 2 ** i * base_2_list[-i-1]
        # print(i,base_2_list[i],y)
        x += y
    return x

def base_10_to_base_2(numb):
    r_list = []

    x = numb
    while x > 0:
        r = x % 2
        q = (x - r)//2
        x = q
        r_list.append(r)

    return r_list[::-1]


def append_leading_zeros(m,n):
    dif = len(m) - len(n)
    n = [0 for i in range(dif)] + n
    return n

def remove_leading_zeros(n):
    j = 0
    while(j < len(n)-1 and n[j] == 0):
        j += 1
    return n[j:]

def is_equal(m,n):
    if len(m) != len(n):
        return False

    i = 0
    while i < len(m) and m[i] == n[i]:
        i += 1
    return i == len(m)

def is_greater(m,n):

    if is_equal(m,n):
        return False

    if len(m) > len(n):
        return True
    elif len(n) > len(m):
        return False
    else:
        i = 0
        while i < len(m) and m[i] == n[i]:
            i += 1
        return m[i] > n[i]

def is_greater_or_equal(m,n):
    return is_greater(m,n) or is_equal(m,n)


def binary_addition(x,y):
    m,n = set_longer_shorter(x,y)
    n = append_leading_zeros(m,n)

    sum_list = []
    sum_result = {
    '000':(0,0), '010':(1,0), '100':(1,0), '110':(0,1),
    '001':(1,0), '011':(0,1), '101':(0,1), '111':(1,1),
    }

    carry = 0
    for i in range(len(m))[::-1]:
        bit_sum = str(m[i]) + str(n[i]) + str(carry)
        value, carry = sum_result[bit_sum]
        sum_list.insert(0,value)

    if carry == 1:
        sum_list.insert(0,1)

    return sum_list

def binary_product(x,y):
    m,n = set_longer_shorter(x,y)

    shifts = []
    list_addends = [[0]]
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

    if len(m) < len(n):
        return [0], m

    q = []
    r = []
    j,i = 0,1
    while(i < len(m)+1): # ?
        d = remove_leading_zeros(r + m[j:i])
        # print(i)
        # print('d',d, 'n',n)
        if is_greater(n,d):
            q.append(0)
        else:
            q.append(1)
            r = binary_subtraction(d,n)
            j = i
        i += 1
        # print('q',q)
        # print('r',r)
        # print('\n')

    if is_greater(n,d):
        r = d

    return remove_leading_zeros(q), r


def binary_power(m,n):

    p = [1]
    a = m

    for i in n[::-1]:
        if i == 1:
            p = binary_product(p,a)
        a = binary_product(a,a)
    return p


def extended_eucludian_algorithm(m,n):
    pass
    # r_k0 = m
    # r_k1 = n
    #
    # r_list = [r_k0, r_k1]
    # a_list = [[1], [0]]
    # b_list = [[0], [1]]
    #
    #
    # while(is_greater(r_k1, [0])):
    #     q_k2, r_k2 = binary_division(r_k0, r_k1)
    #     print(q_k2, r_k2)
    #     r_list.append(r_k2)
    #     a_list.append(binary_subtraction(a_list[-2],binary_product(q_k2, a_list[-1])))
    #     b_list.append(binary_subtraction(b_list[-2],binary_product(q_k2, b_list[-1])))
    #
    #
    #     r_k0 = r_k1
    #     r_k1 = r_k2
    #
    # return r_k0, a_list[-1], b_list[-1]

# def sequence_product():
#     pass
# num_values = 10
# max_value  = 10
# list_values = [base_10_to_base_n(randint(1, max_value)) for i in range(num_values)]
#
# partial_product = list_values[0]
# for i in range(1,len(list_values)):
#     partial_product = binary_product(partial_product, list_values[i])
#
# print(partial_product)

# def sequence_product_modular():
#     pass
