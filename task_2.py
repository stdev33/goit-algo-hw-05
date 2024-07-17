

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == x:
            upper_bound = arr[mid]
            return (iterations, upper_bound)
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
            upper_bound = arr[mid]

    # If the element is not found, the upper_bound will be the next element in the sorted array
    if upper_bound is None and left < len(arr):
        upper_bound = arr[left]

    return (iterations, upper_bound)


sorted_array = [0.2, 0.6, 1.3, 2.9, 3.4, 5.8, 7.9, 9.9]
test_value = 4.1

result = binary_search(sorted_array, test_value)
print(result)
