import collections as co
import timeit
import numpy.random as r

alist = r.randint(1, 100, 10**6)
#alist = ['afsefasesgewgqgqegesfdffeFesfsefsgsegsgaegsaefsefsfe'] * 10**6
s1 = timeit.default_timer()
d1 = co.Counter(alist)
print('collections.Counter runtime : {:.5f} sec'.format(timeit.default_timer() - s1))

s1 = timeit.default_timer()
d2 = {}
for i in alist:
    if i in d2:
        d2[i] += 1
    else:
        d2[i] = 1
print('for loof runtime : {:.5f} sec'.format(timeit.default_timer() - s1))
#print(alist)