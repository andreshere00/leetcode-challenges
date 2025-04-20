## Time Complexity: O(n^2)

from utils.utils import timeit

class Solution(object):
    @timeit()
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

        result = list()
        cont = 0
        for num in self.nums:
            number = [num] * cont
            aux = list(zip(number, self.nums[0:cont]))
            for elem in aux:
                sum = elem[0] + elem[1]
                tup = (elem[0], elem[1]) if elem[0] < elem[1] else (elem[1], elem[0])
                if sum >= self.lower and sum <= self.upper:
                    result.append(tup) 
            cont += 1
        return len(result)
    
sol = Solution()
nums = [0,1,7,4,4,5]; lower = 3; upper = 6
print(sol.countFairPairs(nums, lower, upper) == 6)
nums = [1,7,9,2,5]; lower = 11; upper = 11
print(sol.countFairPairs(nums, lower, upper) == 1)
nums = [0,0,0,0,0,0]; lower = 0; upper = 0
print(sol.countFairPairs(nums, lower, upper) == 15)