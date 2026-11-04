arr = [10, 20, 30, 40, 50, 60, 70]

n = int(input("Enter number to search: "))

low = 0
high = len(arr) - 1
found = False

while low <= high:

    mid = (low + high) // 2

    if arr[mid] == n:
        print("Element found at position:", mid + 1)
        found = True
        break

    elif arr[mid] < n:
        low = mid + 1

    else:
        high = mid - 1

if found == False:
    print("Element not found")
