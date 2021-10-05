import sys
from binary_ops import *

def analyze_func(func_name, m,n):
    tic = time.time()
    func_name(m,n)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t -> Elapsed time: {seconds:.5f}")



m = 2**10000 -1
n = 2**16 -1

analyze_func(binary_addition, base_10_to_base_n(m), base_10_to_base_n(n))
analyze_func(binary_product,  base_10_to_base_n(m), base_10_to_base_n(n))
analyze_func(binary_division, base_10_to_base_n(m), base_10_to_base_n(n))
