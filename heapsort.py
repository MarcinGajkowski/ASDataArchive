import time

import tabele


def heapify(array, size, step):
    largest = step
    left = 2 * step + 1
    right = 2 * step + 2

    if left < size and array[step] < array[left]:
        largest = left

    if right < size and array[largest] < array[right]:
        largest = right

    if largest != step:
        (array[step], array[largest]) = (array[largest], array[step])

        heapify(array, size, largest)


def heapsort(array):
    size = len(array)

    for step in range(size // 2 - 1, -1, -1):
        heapify(array, size, step)

    for step in range(size - 1, 0, -1):
        (array[step], array[0]) = (array[0], array[step])
        heapify(array, step, 0)


start = time.process_time()
heapsort(tabele.arr)
end = time.process_time()
print(tabele.arr)
print(end - start, 'seconds')
time.sleep(5)

start2 = time.process_time()
heapsort(tabele.arr2)
end2 = time.process_time()
print(tabele.arr2)
print(end2 - start2, 'seconds')
time.sleep(5)

start3 = time.process_time()
heapsort(tabele.arr3)
end3 = time.process_time()
print(tabele.arr3)
print(end3 - start3, 'seconds')
