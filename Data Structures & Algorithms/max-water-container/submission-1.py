class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxArea = 0
        while i < j:
            smallerBar = min(heights[i], heights[j])
            currArea = (j - i) * (smallerBar)

            if currArea > maxArea:
                maxArea = currArea
            else:
                if heights[i] < heights[j]:
                    i += 1
                else:
                    j -= 1

        return maxArea