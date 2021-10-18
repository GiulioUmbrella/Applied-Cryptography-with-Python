from binary_ops import *

def signed_multiplication(abs_val_x, abs_val_y, sing_x, sing_y):
    abs_value_product = binary_product(abs_val_x, abs_val_y)

    sign_product = sing_x * sing_y

    return sign_product, abs_value_product


def signed_addition(abs_val_x, abs_val_y, sing_x, sing_y):
    if sing_x == sing_y:
        return sing_x, binary_addition(abs_val_x, abs_val_y)

    # print(abs_val_x)
    # print(abs_val_y)
    # print(sing_x)
    # print(sing_y)

    if is_greater_or_equal(abs_val_x, abs_val_y):
        abs_value = binary_subtraction(abs_val_x, abs_val_y)
        if sing_x >= sing_y:
            sign = 1
        else:
            sign = -1
    else:
        abs_value = binary_subtraction(abs_val_y, abs_val_x)
        if sing_y >= sing_x:
            sign = 1
        else:
            sign = -1

    return sign, abs_value
