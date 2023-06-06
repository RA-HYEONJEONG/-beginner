import sys
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]

def counting_sort(arr):
    # Find the range of input elements
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Initialize count array and sorted array
    count = [0] * range_size
    sorted_arr = [0] * len(arr)

    # Count occurrences of each element
    for num in arr:
        count[num - min_val] += 1

    # Calculate cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the sorted array
    for num in reversed(arr):
        sorted_arr[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return sorted_arr

# Testing the counting_sort function
sorted_arr = counting_sort(numbers)
for element in sorted_arr:
    sys.stdout.write(str(element) + "\n")
