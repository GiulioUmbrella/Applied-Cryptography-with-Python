from binary import *

##### CONSTRUCTOR ######
def test_constructor_empty():
    x = Binary()
    assert x.abs_value == [] and x.sign == None

def test_constructor_pos_int():
    x = Binary(10)
    assert x.abs_value == [1,0,1,0] and x.sign == 1

def test_constructor_neg_int():
    x = Binary(-10)
    assert x.abs_value == [1,0,1,0] and x.sign == -1

def test_constructor_list_pos():
    x = Binary([1,0,1,0],1)
    assert x.abs_value == [1,0,1,0] and x.sign == 1

def test_constructor_list_neg():
    x = Binary([1,0,1,0],-1)
    assert x.abs_value == [1,0,1,0] and x.sign == -1

def test_test():
    x = Binary(2)
    assert x.base10() == 2


def test_constructor_list_with_leading_zero():
    x = Binary([0,1],1)
    assert x.abs_value == [1]

def test_constructor_list_without_leading_zero():
    x = Binary([0],1)
    assert x.abs_value == [0]

def test_base10():
    x = Binary([1,0,1,0],1)
    assert x.base10() == 10


#
def test_binary_addition():
    z = Binary(2) + Binary(2)
    assert z.base10() == 4
#
# def test_binary_subtraction():
#     z = Binary(2) - Binary(2)
#     assert z.base10() == 0
#
def test_binary_multiplication():
    z = Binary(2) * Binary(2)
    assert z.base10() == 4

def test_zero_moltiplication_pos():
    z = Binary(2) * Binary(0)
    assert z.base10() == 0

def test_zero_moltiplication_neg():
    z = Binary(-2) * Binary(0)
    assert z.base10() == 0


#
# def test_binary_multiplicaton_with_zero_dx_sx():
#     z = Binary(0) * Binary(0)
#     assert z.base10() == 0
#
# def test_binary_power():
#     z = Binary(5) ** Binary(2)
#     assert z.base10() == 25

#
# def test_equal():
#     assert Binary(1) == Binary(1)
#
# def test_greater():
#     assert Binary(2) > Binary(1)
#
# def test_greater_or_equal():
#     assert Binary(2) > Binary(1)
