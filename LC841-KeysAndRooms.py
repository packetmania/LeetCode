class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # Surprisingly simple DFS solution
        n = len(rooms)
        visited = set()

        def dfs(room: int):
            if room in visited:
                return
            visited.add(room)
            for key in rooms[room]:
                dfs(key)

        dfs(0)
        return len(visited) == n


# Time complexity: O(N + E) where N is the number of rooms and E is the number of keys
# Space complexity: O(N) for the visited set and the recursion stack

s = Solution()
assert(s.canVisitAllRooms([[1],[2],[3],[]]) == True)
assert(s.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]) == False)