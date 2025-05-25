import numpy as np
def strassness(a, b):
    n = a.shape[0]
    if n == 1:
        return a * b
    mid = n // 2
    a11, a12, a21, a22 = a[:mid, :mid], a[:mid, mid:], a[mid:, :mid], a[mid:, mid:]
    b11, b12, b21, b22 = b[:mid, :mid], b[:mid, mid:], b[mid:, :mid], b[mid:, mid:]
    m1 = strassness(a11+a22,b11+b22)
    m2 = strassness(a21+a22,b11)
    m3 = strassness(a11,b12-b22)
    m4 = strassness(a22,b21-b11)
    m5 = strassness(a11+a12,b22)
    m6 = strassness(a21+a11,b11+b12)
    m7 = strassness(a12+a22,b21+b22)
    c11 = m1 + m4 - m5 + m7
    c12 = m3 + m5
    c21 = m2 + m4
    c22 = m1 - m2 + m3 + m6

    c = np.vstack((np.hstack((c11, c12)), np.hstack((c21, c22))))
    return c
a=[1,4,2,3]
b=[4,5,2,8]
a=np.array(a).reshape(2,2)
b=np.array(b).reshape(2,2)
print(strassness(a,b))
import time
start_time = time.time()
print("Time taken: ", time.time())
