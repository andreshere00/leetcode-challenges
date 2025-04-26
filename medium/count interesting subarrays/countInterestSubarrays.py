# Complexity: O(n^3) 

from typing import List

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        ws = 1
        aux = 0
        while ws <= (len(nums)):
            for n in range(len(nums) - ws + 1):
                subarray = nums[n:n+ws]
                cnt = 0
                for i in range(len(subarray)):
                    if subarray[i] % modulo == k:
                        cnt += 1
                if cnt % modulo == k:
                        cnt = 0; aux += 1
            ws += 1
        return aux     

sol = Solution()
print(sol.countInterestingSubarrays([3,2,4], modulo = 2, k = 1))
print(sol.countInterestingSubarrays([3,1,9,6], modulo = 3, k = 0))