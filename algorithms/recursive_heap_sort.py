def heapify(full_list, n, i):
    largest = i  # Initialize largest as root
    low = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2

    # See if left child of root exists and is
    # greater than root
    if low < n and full_list[i] < full_list[low]:
        largest = low

    # See if right child of root exists and is
    # greater than root
    if r < n and full_list[largest] < full_list[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        full_list[i], full_list[largest] = full_list[largest], full_list[i]

        # Heapify the root.
        heapify(full_list, n, largest)


# The main function to sort an array of given size
def recursive_heap_sort(full_list):
    n = len(full_list)

    # Build a maxheap.
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(full_list, n, i)

    # One by one extract elements
    for i in range(n - 1, 0, -1):
        full_list[i], full_list[0] = full_list[0], full_list[i]   # swap
        heapify(full_list, i, 0)

    return full_list
