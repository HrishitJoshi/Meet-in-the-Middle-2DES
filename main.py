from DES import *

m = b"any long message"
m_1= b"abc deffg djcwij"
cipher = DDES_encrypt(m)
cipher_1 = DDES_encrypt(m_1)


MitM(m, cipher, m_1, cipher_1)