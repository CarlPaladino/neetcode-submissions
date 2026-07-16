class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        solutions = []
        for i in range(len(nums)):
            currResult = 1
            for j in range(len(nums)):
                if i != j:
                    currResult *= nums[j]
            solutions.append(currResult)

        return solutions