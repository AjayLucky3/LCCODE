class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        prefix = 0
        count = 0
        for i in nums:
            prefix += i
            rem = prefix % k
            count += mp.get(rem,0)
            mp[rem] = mp.get(rem,0) +1
        return count