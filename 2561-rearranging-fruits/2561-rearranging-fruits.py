from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total_count = count1 + count2
        
        for fruit, freq in total_count.items():
            if freq % 2 != 0:
                return -1
        
        to_swap = []
        for fruit, freq in total_count.items():
            target = freq // 2
            excess = abs(count1[fruit] - target)
            to_swap.extend([fruit] * excess)
            
        to_swap.sort()
        min_fruit = min(total_count.keys())
        
        cost = 0
        for i in range(len(to_swap) // 2):
            cost += min(to_swap[i], 2 * min_fruit)
            
        return cost