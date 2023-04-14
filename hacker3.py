def find_sum_of_subarrays(arr):
    n = len(arr)  # Length of the input array
    total_sum = 0  # Variable to store the sum of all subarrays

    # Loop through each element in the array
    for i in range(n):
        # Calculate the sum of subarrays starting from the current element
        # and add it to the total sum
        total_sum += arr[i] * (i + 1) * (n - i)

    print(total_sum)

find_sum_of_subarrays([1, 2, 3, 4, 5]) 
