# Write a function find_odd_occurrence(arr) that takes a list of integers and returns the number that occurs an odd number of times.
# The list will always contain only one number that occurs an odd number of times, while all others occur an even number of times.

# Note: Find a solution using O(N) time complexity, where N is the size of the list.

def find_odd_occurrence(arr):
    for i in arr:
        n = arr.count(i)
        if n % 2 != 0 and n > 1:
            odd = i
    print(i)

# Under this line are the data for testing.
arr = [3, 5, -1, 3, 5, -1, 1, 1, 1]
find_odd_occurrence(arr)
