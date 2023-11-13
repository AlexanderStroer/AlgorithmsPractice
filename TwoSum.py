'''
    TwoSum:
    Given an unsorted array as input and a target integer,
    locate two elements in the array that sum up to the target integer.
    If there are no two such numbers, return an empty array

    Time: O(N^2), where N is the number of elements in the array
    Space: O(1)
    
    Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
'''

def twoSum(nums, target):
    for num in range(len(nums)):
        for x in range(num+1, len(nums)):
            if nums[num] + nums[x] == target:
                return [num,x]
