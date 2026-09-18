class Solution(object):
    def frequencySort(self, nums):
        freq ={}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        nums.sort(key=lambda x: (freq[x], -x))
        return nums
        