alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ']

def encipher(plaintext, key):
    enc_msg = []

    for i in plaintext:
        x = (alphabet.index(i) + key) % len(alphabet)
        enc_msg.append(alphabet[x])

    return ''.join(enc_msg)




# key = 10
# m = 'my secret message'
# c = encipher(m, key)
# print(c)
# print(encipher(c, -key))
#
# x = ['a', 'b', 'c', 'd', 'e', 'f']
# print(len(x))
# for i in range(1,len(x)+1):
#     y = []
#     for symbol in x:
#         shift = (x.index(symbol) + i) % len(x)
#         y.append(x[shift])
#         # print(  x[shift], end=' ')
#     print(str(i)+ ' ' + ''.join(y))



from random import randint
k = randint(1,10000000)
m = 'my secret message'
c = encipher(m,k)
print(c)

print(len(alphabet))
for i in range(1,len(alphabet)):
    guess = encipher(c,-i)
        # print(  x[shift], end=' ')
    print(str(i)+ ' ' + guess)
