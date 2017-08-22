def binary_search(arr, key):
    """Given a search key, this binary search function checks if a match found
    in an array of integer.
    Examples:
        - binary_search([3, 1, 2], 2) => True
        - binary_search([3, 1, 2], 0) => False
    Reference: https://en.wikipedia.org/wiki/Binary_search_algorithm

    Args:
        arr (list): A list of integer
        key (int) : Integer search key
    Returns:
        bool: True if key exists in arr, False otherwise
    """
    arr.sort()
    L = 0
    R = len(arr) - 1
    if L > R:
        return False

    mid = R//2
    if key == arr[mid]:
        return True
    elif key < arr[mid]:
        return binary_search(arr[:mid], key)
    else:
        return binary_search(arr[mid+1:], key)
