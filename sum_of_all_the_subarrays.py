def sumSubarrays(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        total_sum += arr[i] * (i + 1) * (n - i)
    print(total_sum)

sumSubarrays([1, 2, 3, 4, 5]) 
