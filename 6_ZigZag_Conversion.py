# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag
# pattern on a given number of rows like this:
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:
            return s
        zigzag = [[] for _ in range(numRows)]
        row = 0
        direction = -1  # -1 for up +1 for down

        for c in s:
            zigzag[row].append(c)
            if row == 0 or row == numRows - 1:
                direction = -direction
            row += direction

        return "".join([c for r in zigzag for c in r])  # flatten list of list
