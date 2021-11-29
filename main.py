import random
import numpy as np
import time

class lazy_dispersion:
    def __init__(self, n):
        self.items = [random.randint(0, 100) for i in range(n)]
        self.n = n
        self.sum = sum(self.items)
        self.mean = self.sum/self.n
    
    def dispersion(self):
        sum2 = 0
        sum3 = 0
        for i in self.lazy_decr():
            sum2 +=i
            sum3 += i**2
        mean2 = sum2/self.n
        mean3 = sum3/self.n
        print("Ленивый подсчет:", mean3)
        
    
    def lazy_decr(self):
        for i in self.items:
            yield abs(i-self.mean)

    
lr1 = lazy_dispersion(5)
#print(lr1.items)
tic = time.perf_counter()
lr1.dispersion()
toc = time.perf_counter()
print(f"Вычисление заняло {toc - tic:0.4f} секунд")

tic = time.perf_counter()
a= np.var(lr1.items)
print("Обычный подсчет: ", a)
toc = time.perf_counter()
print(f"Вычисление заняло {toc - tic:0.4f} секунд")

