# Given an array of ints and a number k, return highest sum of any k consecutive elements in the array.

# Brute force
def brute_highest_sum(arr, k):
    highest_sum = float('-inf')
    n = len(arr)

    # n can't be smaller than k
    if n < k:
        return -1

    # subarray starts at i
    for i in range(n - k + 1):
        # calculate sum of subarray
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]
        # compare sum
        highest_sum = max(highest_sum, current_sum)
    return highest_sum


print(brute_highest_sum([5, -3, 7, -6, 7], 3))


def sliding_window_highest_sum(arr, k):
    highest_sum = float('-inf')
    n = len(arr)

    if n < k:
        return -1

    # compute sum of first windown of size k
    window_sum = sum([arr[i] for i in range(k)])

    # compute sums of remaining windows by removing first element of prev window and adding last element of current window
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        highest_sum = max(highest_sum, window_sum)
    return highest_sum


def highest_sum_two_pointers(arr, k):
    highest_sum = float('-inf')
    n = len(arr)

    if k > n:
        return -1

    left = 0
    right = 0
    window_sum = 0
    while right < n:
        #slide window to right
        window_sum += arr[right]
        right += 1

        #check window sie condition and compare sum
        #drop off left element to avoid oversize
        if right - left == k:
            highest_sum = max(highest_sum, window_sum)
            window_sum -= arr[left]
            left += 1
    return highest_sum




print(sliding_window_highest_sum([5, -3, 7, -6, 8], 3))


#Given a string, find the length of the longest substring without repeating characters
from collections import defaultdict

def longest_unique_substring(s):
    longest_length = float('-inf')
    n = len(s)

    if n == 0:
        return 0

    left = 0
    right = 0
    window = defaultdict(int)
    while right < n:
        #slide window to right
        right_char = s[right]
        window[right_char] += 1
        right +=1

        #if dupe character appears in window, drop off left elements until we have a valid condition
        while window[right_char] > 1:
            window[s[left]] -= 1
            left +=1
        longest_length = max(longest_length, right - left)
    return longest_length

print(longest_unique_substring("pwwkew"))
