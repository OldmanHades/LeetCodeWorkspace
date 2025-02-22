#LeetCode 2958: Make Lexicongraphically Smallest Array by Swapping Elements
# You are given a 0-indexed array of positive integers nums and a postive integer limit.
# In one operation, you can choose any two indices i and j and swap nums[i] and nums [j]
# Return the lexicographically smallest array that can be obtained by performing at most limit operations on nums.
#An array x is lexicographically smaller than an array y if and only if the first different index in the array has a smaller element in x than in y.
# Example 1:
# Input: nums = [1,5,3,9,8], limit = 2
# Output: [1,3,5,8,9]

def lexicographicallySmallestArray(nums, limit):
    n = len(nums)
    # Create pairs of (number, index) to track original positions
    indexed = [(num, i) for i, num in enumerate(nums)]
    # Sort pairs by number
    indexed.sort()
    
    result = [0] * n
    i = 0
    while i < n:
        # Find groups of numbers that can be swapped within limit
        group = [(indexed[i][0], indexed[i][1])]
        while i + 1 < n and abs(indexed[i + 1][1] - indexed[i][1]) <= limit:
            i += 1
            group.append((indexed[i][0], indexed[i][1]))
        
        # Sort indices for current group
        values = sorted([x[0] for x in group])
        indices = sorted([x[1] for x in group])
        
        # Place sorted values at sorted positions
        for val, idx in zip(values, indices):
            result[idx] = val
            
        i += 1
    
    return result

# Example usage
nums = [1,5,3,9,8]
limit = 2
print(lexicographicallySmallestArray(nums, limit))

