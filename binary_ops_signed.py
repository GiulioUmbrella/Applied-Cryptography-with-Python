from binary_ops import *


def signed_multiplication(abs_val_x, abs_val_y, sign_x, sign_y):
    abs_value = binary_product(abs_val_x, abs_val_y)
    sign = sign_x * sign_y

    if abs_value == [0]:
        sign = 1

    return abs_value, sign

def signed_division(abs_val_x, abs_val_y, sing_x, sing_y):
    abs_value = binary_division(abs_val_x, abs_val_y)
    sign = sign_x * sign_y

    if abs_value == [0]:
        sign = 1

    return abs_value, sign


def signed_addition(abs_val_x, abs_val_y, sign_x, sign_y):
    abs_value = []
    sign = 1

    if sign_x == sign_y:
        abs_value = binary_addition(abs_val_x, abs_val_y)
        sign = sign_x

    else:

        if is_greater_or_equal(abs_val_x, abs_val_y):
            abs_value = binary_subtraction(abs_val_x, abs_val_y)
            sign = 1 if sign_x >= sign_y else -1

        else:
            abs_value = binary_subtraction(abs_val_y, abs_val_x)
            sign = 1 if sign_y >= sign_x else -1

    if abs_value == [0]:
        sign = 1

    return abs_value, sign




def signed_is_equal():
    pass

def signed_is_greater():
    pass

def signed_is_greater_or_equal():
    pass



def extended_eucludian_algorithm(m,n):

    r_k0 = m
    r_k1 = n

    # r_list = [r_k0, r_k1]
    # a_list = [[1], [0]]
    # b_list = [[0], [1]]
    #
    #
    while(is_greater(r_k1, [0])):
        q_k2, r_k2 = binary_division(r_k0, r_k1)
    #     print(q_k2, r_k2)
        # r_list.append(r_k2)
        # a_list.append(binary_subtraction(a_list[-2],binary_product(q_k2, a_list[-1])))
        # b_list.append(binary_subtraction(b_list[-2],binary_product(q_k2, b_list[-1])))
    #
    #
        r_k0 = r_k1
        r_k1 = r_k2
    #
    return r_k0
    # return r_k0, a_list[-1], b_list[-1]
