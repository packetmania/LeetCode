class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a > 0 or b > 0 or c > 0:
            abit = a & 1
            bbit = b & 1
            cbit = c & 1

            # Check the bits and determine flips needed
            # abit bbit cbit flips
            #  0    0    0    0
            #  0    1    0    1
            #  1    0    0    1
            #  1    1    0    2
            #  0    0    1    1
            #  0    1    1    0
            #  1    0    1    0
            #  1    1    1    0
            if cbit == 0:
                flips += abit + bbit
            else:
                if abit == 0 and bbit == 0:
                    flips += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flips