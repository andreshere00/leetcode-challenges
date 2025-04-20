## Complexity: O(n) + O(k) -> O(n)

class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        self.answers = answers

        dicto = {}
        for answer in self.answers:
            if answer not in dicto:
                dicto[answer] = 0 
            dicto[answer] = dicto[answer] + 1

        rabbits = 0
        for ans, freq in dicto.items(): 
            num_groups = - ( - freq // (ans+1) ) 
            rabbits += num_groups * (ans + 1)

        return rabbits


sol = Solution()
print(sol.numRabbits(answers=[1,1,3,5,3,5]) == 12)
print(sol.numRabbits(answers=[1,1,2]) == 5)
print(sol.numRabbits(answers=[10,10,10]) == 11)
print(sol.numRabbits(answers=[1,0,1,0,0]) == 5)