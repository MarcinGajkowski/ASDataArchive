class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.current_size = 0

    def moveup(self, u):
        stop = False
        while (u // 2 > 0) and stop is False:
            if self.heap[u] < self.heap[u // 2]:
                self.heap[u], self.heap[u // 2] = self.heap[u // 2], self.heap[u]
            else:
                stop = True
            u = u // 2

    def insert(self, k):
        self.heap.append(k)
        self.current_size += 1
        self.moveup(self.current_size)

    def min_child(self, m):
        if (m * 2) + 1 > self.current_size:
            return m * 2
        else:
            if self.heap[m * 2] < self.heap[(m * 2) + 1]:
                return m * 2
            else:
                return (m * 2) + 1

    def movedown(self, d):
        while d * 2 <= self.current_size:
            mini = self.min_child(d)
            if self.heap[d] > self.heap[mini]:
                self.heap[d], self.heap[mini] = self.heap[mini], self.heap[d]
            d = mini

    def extract_min(self):
        if len(self.heap) == 1:
            return 'Heap emptied'
        root = self.heap[1]
        self.heap[1] = self.heap[self.current_size]
        *self.heap, _ = self.heap
        self.current_size -= 1
        self.movedown(1)
        return root


"""    def minheapify(self, array, size, step):
        smallest = step
        left = 2 * step + 1
        right = 2 * step + 2

        if left < size and array[left] < array[step]:
            smallest = left

        if right < size and array[smallest] < array[right]:
            smallest = right

        if smallest != step:
            (array[step], array[smallest]) = (array[smallest], array[step])

            self.minheapify(array, size, smallest)"""

"""def minheapsort(array):
    size = len(array)

    for step in range(size // 2 - 1, -1, -1):
        minheapify(array, size, step)

    for step in range(size - 1, 0, -1):
        (array[step], array[0]) = (array[0], array[step])
        minheapify(array, step, 0)"""


class Nodes:
    def __init__(self, amount, character, left=None, right=None):
        self.amount = amount
        self.character = character
        self.left = left
        self.right = right
        self.code = ''


def sum_letters(data):
    characters = dict()
    for letter in data:
        if characters.get(letter) is None:
            characters[letter] = 1
        else:
            characters[letter] += 1
    return characters


codes = dict()


def codify(node, value=''):
    newvalue = value + str(node.code)
    if node.left:
        codify(node.left, newvalue)
    if node.right:
        codify(node.right, newvalue)
    if not node.left and not node.right:
        codes[node.character] = newvalue
    return codes


def encode_output(data, coding):
    output = []
    for letter in data:
        print(coding[letter], end='')
        output.append(coding[letter])

    endstring = ''.join([str(letter) for letter in output])

    exit_file = open('compressed.bin', 'ab')
    for letter in output:
        binary = int(letter, base=2)
        exit_file.write(binary.to_bytes(len(letter), "big"))
    exit_file.close()

    exit_file = open('compressed maybe.txt', 'a')
    for letter in output:
        exit_file.write(letter)
    exit_file.close()
    return endstring


def compress_gain(data, code):
    before = len(data) * 8
    after = 0
    chars = code.keys()
    for char in chars:
        count = data.count(char)
        after += count * len(code[char])
    print("Before Huffman: " + str(before) + " bits")
    print("After Huffman: " + str(after) + " bits")


def huff_for_real(data):
    letter_summary = sum_letters(data)
    characters = letter_summary.keys()
    char_counts = letter_summary.values()

    tree_nodes = []
    huff_heap = MinHeap()

    for character in characters:
        times = letter_summary.get(character)
        tree_nodes.append(Nodes(times, character))
        huff_heap.insert(times)

    # for i in huff_heap.heap:
    #     for ch in char_counts:
    #         if i != 0 and i == ch:
    #             for node in tree_nodes:  # nodes ??? + pliki
    #                 tree_nodes.pop(huff_heap.heap.index(ch))
    #                 tree_nodes.insert(huff_heap.heap.index(ch)-1, Nodes(i, node.character))

    while len(tree_nodes) > 1:
        amounts = []
        for node in tree_nodes:
            amounts.append(node.amount)
            print(node.character, node.amount)

        left = huff_heap.extract_min()
        right = huff_heap.extract_min()
        r_node = tree_nodes[0]
        l_node = tree_nodes[1]

        # for node in tree_nodes:
        #     if node.amount == left:
        #         l_node = node
        #     else:
        #         if node.amount == right:
        #             r_node = node
        #             break

        l_node.code = 0
        r_node.code = 1

        newnode = Nodes(l_node.amount + r_node.amount, l_node.character + r_node.character, l_node, r_node)
        huff_heap.insert(left + right)

        tree_nodes.remove(l_node)
        tree_nodes.remove(r_node)
        tree_nodes.append(newnode)

    encoding = codify(tree_nodes[0])
    compress_gain(data, encoding)
    print("coded characters: ", encoding)
    encoded_output = encode_output(data, encoding)

    return encoded_output


def convert_file(path):
    entry_file = open(path)
    huff_for_real(entry_file.read())


sample = "2,000 kanji. 6,000 vocabulary words. In just over a year."
final_code = huff_for_real(sample)
convert_file("sampletext.txt")
print("encoded output: ", final_code)
