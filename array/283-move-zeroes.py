# Given an array nums, write a function to move all 0's to the end of it while maintaining 
# the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) == 0: return
        index = 0
        for n in nums:
            if n != 0:
                nums[index] = n
                index += 1

        while index < len(nums):
            nums[index] = 0
            index += 1
        

solution = Solution()
nums = [0,1,0,3,12]
solution.moveZeroes(nums)
print(nums)        
