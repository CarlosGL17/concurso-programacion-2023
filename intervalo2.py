from memory_profiler import memory_usage_psutil
import time
inicio = time.time()
def mayor(lista):
    max = lista[0];
    for x in lista:
        if x > max:
            max = x
    return max    
 
def menor(lista):
    min = lista[0];
    for x in lista:
        if x < min:
            min = x
    return min
list=[1,2,3,4,5,6,7,8,9,10]
print(mayor(list))
print(menor(list))

#matriz
list = [list(map(int, input().split())) for _ in range(3)]