import heapq


def heapify(array: list[int], idx: int = 0):
    if idx < len(array):
        left = 2 * idx + 1
        right = 2 * idx + 2
        parent_node = array[idx]
        largest = idx
        if left < len(array) and array[left] > parent_node:
            largest = left
        if (
            right < len(array)
            and array[right] > parent_node
            and array[right] > array[left]
        ):
            largest = right

        if largest != idx:
            array[idx], array[largest] = array[largest], array[idx]
            heapify(array, largest)


def heapsort(array: list[int]):
    pass


if __name__ == "__main__":
    x = [
        2,
        4,
        5,
        6,
        3,
        1,
        4,
        4,
        4,
        4,
        4,
        453,
        322,
        21312,
        322342352,
        12,
        2414,
        4534,
        5345,
    ]
    for i in range(0, len(x)):
        j = len(x) - 1 - i
        heapify(x, j)
    print(x)
    print(heapq.heapify(x))
    print(x)

# end main
