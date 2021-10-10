from binary import *

##### CONSTRUCTOR ######
def test_constructor_empty():
    x = Binary()
    assert x.value == []

def test_constructor_int():
    x = Binary(10)
    assert x.value == [1,0,1,0]

def test_constructor_list():
    x = Binary([1,0,1,0])
    assert x.value == [1,0,1,0]

def test_constructor_list_with_leading_zero():
    x = Binary([0,1])
    assert x.value == [1]

def test_constructor_list_without_leading_zero():
    x = Binary([0])
    assert x.value == [0]

def test_base10():
    x = Binary([1,0,1,0])
    assert x.base10() == 10

#### BINARY OPERATIONS ####

def test_binary_addition():
    z = Binary(2) + Binary(2)
    assert z.base10() == 4

def test_binary_subtraction():
    z = Binary(2) - Binary(2)
    assert z.base10() == 0

def test_binary_multiplicaton():
    z = Binary(2) * Binary(2)
    assert z.base10() == 4

def test_binary_multiplicaton_with_zero():
    z = Binary(2) * Binary(2)
    assert z.base10() == 4

def test_binary_multiplicaton_with_zero_dx():
    z = Binary(2) * Binary(0)
    assert z.base10() == 0

def test_binary_multiplicaton_with_zero_sx():
    z = Binary(0) * Binary(2)
    assert z.base10() == 0

def test_binary_multiplicaton_with_zero_dx_sx():
    z = Binary(0) * Binary(0)
    assert z.base10() == 0

def test_binary_power():
    z = Binary(5) ** Binary(2)
    assert z.base10() == 25


def test_equal():
    assert Binary(1) == Binary(1)

def test_greater():
    assert Binary(2) > Binary(1)

def test_greater_or_equal():
    assert Binary(2) > Binary(1)


#
#
# m = base_10_to_base_n(27)
# n = base_10_to_base_n(3)
# print(m)
# print(n)
# print(binary_product(m,n))
# print(binary_division(m,n))
# print(binary_mod(m,n))


###### Greater or equal

# x = Binary(10)
# y = Binary(2)
# z = x - y
# print(type(x))
# print(type(y))
# print(type(z))
# print(x)
# print(y)
# print(z)


# x = Binary(1)
# y = Binary(11)
# print(x > y)


# DIVISION TEST
# # return a reminder when d is less than n at the end of the while loop
# x = base_10_to_base_n(5)
# y = base_10_to_base_n(2)
# binary_division(x, y)
# # 1 zero reminder check
# # 5 / 2
#

#
#
#
# def test_values(a,b,test_values):
#
#     x = [randint(a+1, b) for i in range(test_values)]
#     y = [randint(1, a) for i in range(test_values)]
#
#     numb_err = 0
#     for i,j in zip(x,y):
#
#         diff_base_10 = i-j
#         diff_base_2 = binary_subtraction(base_10_to_base_n(i),
#         base_10_to_base_n(j))
#         diff_base_10_check = base_2_to_10(diff_base_2)
#
#         if diff_base_10 != diff_base_10_check:
#             numb_err += 1
#
#     print('total number of error',numb_err)
