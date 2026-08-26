class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        req_list = []
        for i in matrix:
            x = 0
            for j in i:
                x += j
            req_list.append(x)
        return req_list