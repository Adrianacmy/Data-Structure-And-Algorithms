# worst case n2 (unbalanced partition)
# average runtime of randomalzied quick sort is nlogn(balanced partition)
# effient for large datasets

def quicksort(arr):
    """ Quicksort a list
    :type arr: list
    :param arr: List to sort
    :returns: list -- Sorted list
    """
    if not arr:
        return []

    pivots = [x for x in arr if x == arr[0]]
    lesser = quicksort([x for x in arr if x < arr[0]])
    greater = quicksort([x for x in arr if x > arr[0]])

    return lesser + pivots + greater