import sys
import time
from binary_ops import *

def analyze_func(func_name, m,n):
    tic = time.time()
    func_name(m,n)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t -> Elapsed time: {seconds:.5f}")

m = cambio_di_base(int(sys.argv[1]))
n = cambio_di_base(int(sys.argv[2]))

# analyze_func(binary_sum, m,n)
# analyze_func(binary_product, m,n)
# a,b,c = binary_product(m,n)
ops, sum_value = binary_sum(m,n)
print(ops)
print(sum_value)


ops, list_addends, partial_sums = binary_product(m,n)
print(list_addends)
print(ops)
print(partial_sums)
