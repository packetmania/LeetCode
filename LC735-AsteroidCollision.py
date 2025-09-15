class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        # Solution with stack, note the collision would happen if
        # the previous one is + and the current one is -.
        stack = []

        for x in asteroids:
            push = True
            while stack and (stack[-1] > 0 and x < 0):
                # collision happens
                if abs(x) < stack[-1]:
                    # no push, new one explodes
                    push = False
                    break
                elif abs(x) == stack[-1]:
                    # both will explode, stack pop
                    stack.pop()
                    push = False
                    break
                else:
                    # the new one has bigger size, stack pop
                    push = True
                    stack.pop()

            if push:
                stack.append(x)  # stack push

        return stack


# Time complexity: O(n)
# Space complexity: O(n)

s = Solution()
assert(s.asteroidCollision([5,10,-5]) == [5,10])
assert(s.asteroidCollision([8,-8]) == [])
assert(s.asteroidCollision([10,2,-5]) == [10])