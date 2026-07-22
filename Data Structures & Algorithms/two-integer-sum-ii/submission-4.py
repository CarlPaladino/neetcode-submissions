class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        firstIndex = 0
        secondIndex = len(numbers) - 1
        while firstIndex < secondIndex:
            current = numbers[firstIndex] + numbers[secondIndex]

            if current > target:
                secondIndex -= 1
            elif current < target:
                firstIndex += 1
            else:
                return[firstIndex + 1, secondIndex + 1]
