class Solution:
    def reorganizeString(self, s: str) -> str:
        
        from collections import Counter
        import heapq

        freq = Counter(s)
        heap =[(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)
        result = []
        prev_count = 0
        prev_char =""

        while heap:
            count, char = heapq.heappop(heap)
            result.append(char)
            count += 1
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))
            prev_count = count
            prev_char = char
        if len(result) != len(s):
            return ""
        return "".join(result)