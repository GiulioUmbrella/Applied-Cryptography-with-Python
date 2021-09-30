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

m = cambio_di_base(int(sys.argv[1]))
n = cambio_di_base(int(sys.argv[2]))


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
num_values = 10
max_value  = 10
list_values = randint(num_values, max_value)
x =
for i in list_values:



#### MODULAR PRODUCT ####
