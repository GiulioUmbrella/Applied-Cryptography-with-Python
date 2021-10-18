from signed_binary_ops import *

# # PRODOTTO
# def test_product_0():
#     x = base_10_to_base_2(2)
#     y = base_10_to_base_2(2)
#     sign, abs_value_product = signed_multiplication(x,y,1,1)
#     product = base_2_to_base_10(abs_value_product)
#
#     assert sign == 1 and product == 4
#
# def test_product_1():
#     x = base_10_to_base_2(2)
#     y = base_10_to_base_2(2)
#     sign, abs_value_product = signed_multiplication(x,y,1,-1)
#     product = base_2_to_base_10(abs_value_product)
#
#     assert sign == -1 and product == 4
#
# def test_product_2():
#     x = base_10_to_base_2(2)
#     y = base_10_to_base_2(2)
#     sign, abs_value_product = signed_multiplication(x,y,-1,1)
#     product = base_2_to_base_10(abs_value_product)
#
#     assert sign == -1 and product == 4
#
#
# def test_product_3():
#     x = base_10_to_base_2(2)
#     y = base_10_to_base_2(2)
#     sign, abs_value_product = signed_multiplication(x,y,-1,-1)
#     product = base_2_to_base_10(abs_value_product)
#
#     assert sign == 1 and product == 4
#
#
# # TEST SOMMA
# def test_sum_0():
#     x = base_10_to_base_2(3)
#     y = base_10_to_base_2(2)
#     sign, abs_value_sum = signed_addition(x,y,1,1)
#     sum = base_2_to_base_10(abs_value_sum)
#
#     assert sign == 1 and sum == 5
#
# def test_sum_1():
#     x = base_10_to_base_2(3)
#     y = base_10_to_base_2(2)
#     sign, abs_value_sum = signed_addition(x,y,-1,-1)
#     sum = base_2_to_base_10(abs_value_sum)
#
#     assert sign == -1 and sum == 5
#
#
def test_sum_2():
    x = base_10_to_base_2(3)
    y = base_10_to_base_2(2)
    abs_value_sum, sign = signed_addition(x,y,-1,1)
    sum = base_2_to_base_10(abs_value_sum)

    assert sign == -1 and sum == 1

def test_sum_3():
    x = base_10_to_base_2(3)
    y = base_10_to_base_2(2)
    abs_value_sum, sign = signed_addition(x,y,1,-1)
    sum = base_2_to_base_10(abs_value_sum)

    assert sign == 1 and sum == 1

def test_sum_4():
    x = base_10_to_base_2(2)
    y = base_10_to_base_2(3)
    abs_value_sum, sign = signed_addition(x,y,1,-1)
    sum = base_2_to_base_10(abs_value_sum)

    assert sign == -1 and sum == 1
