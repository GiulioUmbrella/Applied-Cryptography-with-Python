x = [0]
print(remove_leading_zeros(x))

y = [0,0,1]
print(remove_leading_zeros(y))

z = [1]
print(remove_leading_zeros(z))


m = base_10_to_base_n(27)
n = base_10_to_base_n(3)
print(m)
print(n)
print(binary_product(m,n))
print(binary_division(m,n))
print(binary_mod(m,n))


def test_values(a,b,test_values):

    x = [randint(a+1, b) for i in range(test_values)]
    y = [randint(1, a) for i in range(test_values)]

    numb_err = 0
    for i,j in zip(x,y):

        diff_base_10 = i-j
        diff_base_2 = binary_subtraction(base_10_to_base_n(i),
        base_10_to_base_n(j))
        diff_base_10_check = base_2_to_10(diff_base_2)

        if diff_base_10 != diff_base_10_check:
            numb_err += 1

    print('total number of error',numb_err)
