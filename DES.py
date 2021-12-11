

from des import *


# We'll have 2DES implementation here
def DDES_encrypt(m):
    a = 200
    b = 220
    byt = a.to_bytes(8, 'little')
    byt2 = b.to_bytes(8, 'little')
    key = DesKey(byt)
    key2 = DesKey(byt2)
    middle = key.encrypt(m)
    c = key2.encrypt(middle)
    return c

# because 0x0000fff is 4095 that's our key range according to question
# because it is mentioned that we ignore the first 32 bit of the 56 bit key which is ust 3 bytes. hence 0xfff = 4095
# now we do the attack

def MitM(m, c, m1, c1):
    mid = [0] * 4095
    mid_1 = [0] * 4095
    0

    for i in range(0,4095,1):
        byte = i.to_bytes(8, 'little')
        k = DesKey(byte)
        mid[i] = k.encrypt(m)
        mid_1[i] = k.encrypt(m1)

    for i in range(0,4095,1):
        byte1 = i.to_bytes(8, 'little')
        k1 = DesKey(byte1)
        middletext = k1.decrypt(c)
        middletext_1 = k1.decrypt(c1)
        for j in range(0,4095,1):
            if mid[j] == middletext:
                print("key 1 is", j)
                print("key 2 is", i)
                return 0
        for j in range(0,4095,1):
            if mid_1[j] == middletext_1:
                print("key 1 is", j)
                print("key 2 is", i)
                return 0




