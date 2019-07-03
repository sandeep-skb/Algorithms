'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# Fundamental Idea here is use a hashmap since the search time is constant. 
# If the target - n does not exist, then push n into the map along with index. 
# later down in the array the compliment would be the element stored in the dictionary if the 2 sum actually exists.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        index = 0

        for idx,n  in enumerate(nums):
            if (target - n) in compliments.keys():
                return([compliments[target - n], idx])
            else:
                compliments[n] = idx
        return []
