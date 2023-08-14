def find_subarray(A, S):
    n = len(A)
    current_sum = A[0]
    left = 0
    right = 1

    while right <= n:
        while current_sum > S and left < right-1:
            current_sum -= A[left]
            left += 1

        if current_sum == S:
            return [left+1, right]

        if right < n:
            current_sum += A[right]
        right += 1

    return [-1]

# Example usage
A = [1, 2, 3, 7, 5]
S = 12
print(find_subarray(A, S)) # Output: [-1]