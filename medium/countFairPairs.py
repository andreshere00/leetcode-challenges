## Time Complexity: O(n^2)

def lower_bound(nums, target, start):
    end = len(nums)
    while start < end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start

def upper_bound(nums, target, start):
    end = len(nums)
    while start < end:
        mid = (start + end) // 2
        if nums[mid] > target:
            end = mid
        else:
            start = mid + 1
    return start

class Solution(object):
    def countFairPairs(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """

        self.nums = nums
        self.lower = lower
        self.upper = upper

        self.nums.sort()
        count = 0
        
        for i in range(len(self.nums)):
            left = lower_bound(self.nums, lower - nums[i], i + 1)
            right = upper_bound(self.nums, upper - nums[i], i + 1)
            count += right - left
        return count
    
sol = Solution()
nums = [0,1,7,4,4,5]; lower = 3; upper = 6
print(sol.countFairPairs(nums, lower, upper) == 6)
nums = [1,7,9,2,5]; lower = 11; upper = 11
print(sol.countFairPairs(nums, lower, upper) == 1)
nums = [0,0,0,0,0,0]; lower = 0; upper = 0
print(sol.countFairPairs(nums, lower, upper) == 15)