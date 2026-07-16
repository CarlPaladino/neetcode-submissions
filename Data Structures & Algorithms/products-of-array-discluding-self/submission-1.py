class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        solutions = [1] * n
        
        left = 1
        for i in range(n):
            solutions[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(n - 1, -1, -1):
            solutions[i] *= right
            right *= nums[i]

        return solutions