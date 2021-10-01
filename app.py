import sys
import time
from random import randint
from binary_ops import *


def analyze_func(func_name, m,n):
    tic = time.time()
    func_name(m,n)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t -> Elapsed time: {seconds:.5f}")

def test_values(a,b,test_values):

    x = [randint(a+1, b) for i in range(test_values)]
    y = [randint(1, a) for i in range(test_values)]

    numb_err = 0
    for i,j in zip(x,y):

        diff_base_10 = i-j
        diff_base_2 = binary_subtraction(cambio_di_base(i),
        cambio_di_base(j))
        diff_base_10_check = base_2_to_10(diff_base_2)

        if diff_base_10 != diff_base_10_check:
            numb_err += 1

    print('total number of error',numb_err)

# test_values(1000, 10000, 5000)


analyze_func(binary_subtraction, cambio_di_base(99999999), cambio_di_base(99999))

#### 1 TIME COMPLEXITY #####

# analyze_func(binary_sum, m,n)
# analyze_func(binary_product, m,n)
# a,b,c = binary_product(m,n)

#### 2 PRODUCT COMPLEXITY ####
# ops, list_addends, partial_sums = binary_product(m,n)
# print(ops)
# for i in list_addends:
#     print(i)
# print(partial_sums)

#### 3 PRODUCT ####
# num_values = 10
# max_value  = 10
# list_values = [cambio_di_base(randint(1, max_value)) for i in range(num_values)]
#
# partial_product = list_values[0]
# for i in range(1,len(list_values)):
#     partial_product = binary_product(partial_product, list_values[i])
#
# print(partial_product)

#### SUBTRACTION ####
# from random import randint
#
# x = [randint(100001, 5000000) for i in range(10000)]
# y = [randint(1, 10000) for i in range(10000)]
#
# numb_err = 0
# for i,j in zip(x,y):
#
#     diff_base_10 = i-j
#     diff_base_2 = binary_subtraction(cambio_di_base(i),
#     cambio_di_base(j))
#     diff_base_10_check = base_2_to_10(diff_base_2)
#
#     if diff_base_10 != diff_base_10_check:
#         numb_err += 1
#
# print('total number of error',numb_err)
    # else:
    #     print(f"{i} - {j} OK")
# m = cambio_di_base(int(sys.argv[1]))
# n = cambio_di_base(int(sys.argv[2]))
# print(int(sys.argv[1]), m)
# print(int(sys.argv[2]), n)
#
#
# x = binary_subtraction(m,n)
# print(x)
# print(base_2_to_10(x))
# print(str(int(sys.argv[1])-int(sys.argv[2])))
# print(cambio_di_base(int(sys.argv[1])-int(sys.argv[2])))

#### MODULAR PRODUCT ####
