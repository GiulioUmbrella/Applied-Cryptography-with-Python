import sys
from binary_ops import *

m = 2**10000 -1
n = 2**16 -1

analyze_func(binary_addition, base_10_to_base_n(m), base_10_to_base_n(n))
analyze_func(binary_product,  base_10_to_base_n(m), base_10_to_base_n(n))
analyze_func(binary_division, base_10_to_base_n(m), base_10_to_base_n(n))
