# 1. Two Sum
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]


# LeetCode Problem: Two Sum# Problem Link: https://leetcode.com/problems/two-sum/ Best Solution
# 1. Two Sum
class Solution(object):
    def twoSum(self, nums, target):
        seen= {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] =i
# Problem Link: https://leetcode.com/problems/two-sum/
    


# My Solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i in range(0,len(nums)-1):
            for j in range(0,len(nums)-1):
                if nums[i] + nums[j+1] == target and i!=j+1:
                    res.append(i)
                    res.append(j+1)
                    return res