from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        answer = True
        elements = set(arr)
        counters = Counter(arr)
        freqencie = set()
        for i in elements:
            if counters[i] in freqencie:
                answer = False
                break
            else:
                freqencie.add(counters[i])
        return answer


# Time complexity: O(n)
# Space complexity: O(n)

s = Solution()
assert(s.uniqueOccurrences([1,2,2,1,1,3]) == True)
assert(s.uniqueOccurrences([1,2]) == False)
assert(s.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0]) == True)