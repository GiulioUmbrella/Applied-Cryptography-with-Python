# Euclidian Algorithm
import sys

u = int(sys.argv[1])
v = int(sys.argv[2])

r_k  = int(u)
r_k1 = int(v)
while(r_k1 > 0):
    r_k2 = r_k % r_k1
    q_k2 = r_k // r_k1
    print(f"({r_k}, {r_k1}) \t q = {q_k2}, r = {r_k2}")
    if r_k2 == 0:
        break
    else:
        r_k  = r_k1
        r_k1 = r_k2

print(f"gcd {u} and {v} is {r_k1}")
