def heapify_util(arr, n, idx):
    if idx < n:
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != idx:
            arr[idx], arr[largest] = arr[largest], arr[idx]
            heapify_util(arr, n, largest)


def heapify(arr):
    """
    Starting at the last non-leaf node
    - Root at 0
    - Left child at 2*i + 1
    - Right child at 2*i + 2
    - O(n):
        number of nodes halves going up in level
        number of total nodes scales linearly with max no of leaf nodes
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify_util(arr, n, i)


def heapsort(arr):
    # O(nlogn)

    # Make max heap
    heapify(arr)

    #
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify_util(arr, i, 0)


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
    heapsort(x)
    print(x)
