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
        diff_base_2 = binary_subtraction(base_10_to_base_n(i),
        base_10_to_base_n(j))
        diff_base_10_check = base_2_to_10(diff_base_2)

        if diff_base_10 != diff_base_10_check:
            numb_err += 1

    print('total number of error',numb_err)
