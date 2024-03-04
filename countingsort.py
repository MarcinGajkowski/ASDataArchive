# counting sort wydawał się najbardziej przyjemny
import time

import tabele


def countingsort(array):
    size = len(array)
    output = [0] * size

    count = [0] * (max(array) + 1)

    for i in range(0, size):
        count[array[i]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


start = time.process_time()
countingsort(tabele.arr)
end = time.process_time()
print(tabele.arr)
print(end - start, ' seconds')
time.sleep(5)

start2 = time.process_time()
countingsort(tabele.arr2)
end2 = time.process_time()
print(tabele.arr2)
print(end2 - start2, ' seconds')
time.sleep(5)

start3 = time.process_time()
countingsort(tabele.arr3)
end3 = time.process_time()
print(tabele.arr3)
print(end3 - start3, ' seconds')
