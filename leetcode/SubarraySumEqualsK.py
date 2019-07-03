'''
https://leetcode.com/problems/subarray-sum-equals-k/
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Idea here is (x + k) = Sum
        # so, (Sum - k) = x
        # "x" here is the some previous running sum. If this x exists in the
        #running sum of the array, then
        # it can be considered to be a continuous subarray whose sum = k
        sum_track = {0:1} # if the element itself == k that needs to be also counted.
        count = 0
        tot = 0
        for num in nums:
            tot += num
            count += sum_track.get((tot-k),0)
            sum_track[tot] = sum_track.get(tot, 0) + 1
            #print("tot: {}, count: {}, sum_track: {}".format(tot, count, sum_track))
        return count
                
        
