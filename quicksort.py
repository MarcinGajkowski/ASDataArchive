import time

import tabele


def partition(a, p, r):
    pivot = a[r]
    smaller = p
    for j in range(p, r):
        if a[j] <= pivot:
            a[smaller], a[j] = a[j], a[smaller]
            smaller = smaller + 1
    a[smaller], a[r] = a[r], a[smaller]
    return smaller


def quicksort(a, p, r):
    if p < r:
        q = partition(a, p, r)
        quicksort(a, p, q - 1)
        quicksort(a, q + 1, r)


start = time.process_time()
quicksort(tabele.arr, 0, 99999)
end = time.process_time()
print(tabele.arr)
print(end - start, 'seconds')
time.sleep(5)

start2 = time.process_time()
quicksort(tabele.arr2, 0, 99999)
end2 = time.process_time()
print(tabele.arr2)
print(end2 - start2, 'seconds')
time.sleep(5)

start3 = time.process_time()
quicksort(tabele.arr3, 0, 99999)
end3 = time.process_time()
print(tabele.arr3)
print(end3 - start3, 'seconds')
