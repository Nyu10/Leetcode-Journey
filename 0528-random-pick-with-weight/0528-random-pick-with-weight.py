import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.prefixSum = []
        self.totalSum = 0
        curSum = 0
        for val in w:
            curSum += val
            self.prefixSum.append(curSum)
        self.totalSum = curSum

    def pickIndex(self) -> int:
        valToSearchFor = random.uniform(0, self.totalSum)
        return bisect.bisect(self.prefixSum, valToSearchFor)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()