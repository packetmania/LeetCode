from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # Solution with two double-ended queues

        queue_r, queue_d = deque(), deque()
        n = len(senate)

        # build up two queues with the index
        for i, senator in enumerate(senate):
            if senator == 'R':
                queue_r.append(i)
            else:
                queue_d.append(i)

        r_index, d_index = 0, 0  # queue indexes

        while queue_r and queue_d:
            r_index = queue_r.popleft()
            d_index = queue_d.popleft()

            if r_index < d_index:
                # Radiant senator is earlier, ban Dire senator
                # and enqueue for next round
                queue_r.append(r_index + n)

            else:
                # Dire senator is earlier, ban Radiant senator
                # and enqueue for next round
                queue_d.append(d_index + n)

        return "Radiant" if not queue_d else "Dire"


# Time complexity: O(n)
# Space complexity: O(n)

s = Solution()
assert(s.predictPartyVictory("RD") == "Radiant")
assert(s.predictPartyVictory("RDD") == "Dire")