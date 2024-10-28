class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0:1} #0 sum occurs once
        currentSum = 0
        count = 0

        for num in nums:
            currentSum += num

            if currentSum - k in prefixSums:
                count += prefixSums[currentSum - k]
            prefixSums[currentSum] = prefixSums.get(currentSum, 0) + 1

        return count