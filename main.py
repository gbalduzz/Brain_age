from modules import file_IO, preprocessing
import numpy as np
from multiprocessing.dummy import Pool as ThreadPool

N=5
x = np.zeros(5)

def say_hi(n):
    x[0] += n
    print("hi", n)
threads= 4
pool = ThreadPool(threads)

pool.map(say_hi,range(N))
print("x", x)
