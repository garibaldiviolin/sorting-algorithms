def partition(arr, low, h):
    i = (low - 1)
    x = arr[h]

    for j in range(low, h):
        if arr[j] <= x:

            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return (i + 1)


# Function to do Quick sort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# h  --> Ending index
def iteractive_quick_sort(arr, low=0, h=None):
    if h is None:
        h = len(arr) - 1

    # Create an auxiliary stack
    size = h - low + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of low and h to stack
    top = top + 1
    stack[top] = low
    top = top + 1
    stack[top] = h

    # Keep popping from stack while is not empty
    while top >= 0:

        # Pop h and low
        h = stack[top]
        top = top - 1
        low = stack[top]
        top = top - 1

        # Set pivot element at its correct position in
        # sorted array
        p = partition(arr, low, h)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p - 1 > low:
            top = top + 1
            stack[top] = low
            top = top + 1
            stack[top] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < h:
            top = top + 1
            stack[top] = p + 1
            top = top + 1
            stack[top] = h

    return arr
