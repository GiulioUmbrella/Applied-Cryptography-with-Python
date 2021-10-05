import sys
from binary_ops import *

def analyze_func(func_name, m,n):
    tic = time.time()
    func_name(m,n)
    toc = time.time()
    seconds = toc - tic
    print(f"{func_name.__name__.capitalize()}\t -> Elapsed time: {seconds:.5f}")


######## BASIC OPERATION #######
m = 2**10000 -1
n = 2**16 -1

analyze_func(binary_addition, base_10_to_base_n(m), base_10_to_base_n(n))
analyze_func(binary_product,  base_10_to_base_n(m), base_10_to_base_n(n))
analyze_func(binary_division, base_10_to_base_n(m), base_10_to_base_n(n))


######### PRODUTTORIA ###########
def numb_seq_generator(max_value, tot_values):
    return [base_10_to_base_n(randint(1, max_value)) for i in range(tot_values)]

max_value = 10
tot_values = 1000
mod_value = base_10_to_base_n(1000)

seq = numb_seq_generator(max_value, tot_values)
# print(seq)

p = [1]
tic = time.time()
for i in seq:
    p = binary_product(p, i)
toc = time.time()
seconds = toc - tic
print(seconds)
