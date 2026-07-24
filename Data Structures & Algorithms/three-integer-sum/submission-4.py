class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        distinctTriplets = []

        i = 0

        while i < len(sortedNums):

            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = len(sortedNums) - 1

            while j < k:

                if j > i + 1 and sortedNums[j] == sortedNums[j - 1]:
                    j += 1
                    continue

                total = sortedNums[i] + sortedNums[j] + sortedNums[k]

                if total > 0:
                    k -= 1

                elif total < 0:
                    j += 1

                else:
                    distinctTriplets.append(
                        [sortedNums[i], sortedNums[j], sortedNums[k]]
                    )

                    j += 1
                    k -= 1

                    while j < k and sortedNums[j] == sortedNums[j - 1]:
                        j += 1

                    while j < k and sortedNums[k] == sortedNums[k + 1]:
                        k -= 1

            i += 1

        return distinctTriplets