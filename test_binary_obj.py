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
