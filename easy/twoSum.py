# Complexity: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        self.nums = nums
        self.target = target

        if (abs(self.target) > 10**9) or (len(self.nums) < 2) or (len(self.nums) > 10**4):
            return

        seen = {}
        for i, num in enumerate(self.nums):
            complement = self.target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return
        
sol = Solution()            

print(sol.twoSum(nums = [2,7,11,15], target = 9) == [0,1])
print(sol.twoSum(nums = [3,2,4], target = 6) == [1,2])
print(sol.twoSum(nums = [3,3], target = 6) == [0,1])
print(sol.twoSum(nums = [-1,-2,-3,-4,-5], target = -8) == [2,4])
print(sol.twoSum(nums = [-1,-8,-5,-7,-3], target = -8) == [0,3])