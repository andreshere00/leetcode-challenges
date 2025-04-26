from typing import List

class Algorithm:
    def sequential_search(self, nums: List[int], target: int) -> int:
        """
        Find the index of the target element.

        Arguments:
        - nums: the array of numbers.
        - target: the number to be searched.

        Returns:
        - The position of the target within the nums array.
        """

        for i in range(len(nums)):
            if nums[i] == target:
                return i
        
        return f"Target is not presented in {nums}."
    
alg = Algorithm()
print(alg.sequential_search(nums = [1,2,6,3,2,8,21,59], target = 21))