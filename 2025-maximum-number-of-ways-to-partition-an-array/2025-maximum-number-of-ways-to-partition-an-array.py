from collections import Counter
from typing import List

class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        total = sum(nums)

        right = Counter()
        prefix = 0

        for i in range(len(nums) - 1):
            prefix += nums[i]
            right[prefix] += 1

        left = Counter()

        ans = right[total // 2] if total % 2 == 0 else 0

        prefix = 0

        for i in range(len(nums)):
            x = nums[i]
            diff = k - x

            target = total + diff

            before = 0
            if target % 2 == 0:
                before = left[target // 2]

            target = total - diff

            after = 0
            if target % 2 == 0:
                after = right[target // 2]

            ans = max(ans, before + after)

            if i < len(nums) - 1:
                prefix += x

                right[prefix] -= 1
                if right[prefix] == 0:
                    del right[prefix]

                left[prefix] += 1

        return ans