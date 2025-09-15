class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        from math import inf
        smaller, smallest = inf, inf

        # Iterate through the array.
        for num in nums:
            # If the current number is less than or equal to 'smallest',
            # it becomes the new smallest number.
            if num <= smallest:
                smallest = num
            # If the current number is greater than 'smallest' but less than
            # or equal to 'smaller', it becomes the new smaller number.
            elif num <= smaller:
                smaller = num
            # If the current number is greater than both 'smallest'
            # and 'smaller', we have found an increasing triplet.
            else:
                return True

        # If no such triplet is found after iterating through
        # the entire array, return False.
        return False


# Time complexity: O(n)
# Space complexity: O(1)

s = Solution()
assert(s.increasingTriplet([1,2,3,4,5]) == True)
assert(s.increasingTriplet([5,4,3,2,1]) == False)
assert(s.increasingTriplet([2,1,5,0,4,6]) == True)