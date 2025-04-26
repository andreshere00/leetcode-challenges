from typing import List

class Algorithm:
    def binary_search(self, nums: List[int], target: int) -> int:
        """
        Find the index of the target element.

        Arguments:
        - nums: the array of numbers (must be sorted).
        - target: the number to be searched.

        Returns:
        - The position of the target within the nums array. If not found, returns -1.
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

alg = Algorithm()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(alg.binary_search(nums, target))