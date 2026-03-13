# Binary search algorithm

numbers = [3, 7, 12, 18, 25, 31, 42]
target = 18

left = 0
right = len(numbers) - 1

found = False

while left <= right:
    mid = (left + right) // 2

    if numbers[mid] == target:
        found = True
        break
    elif numbers[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

if found:
    print("Element found at index", mid)
else:
    print("Element not found")
