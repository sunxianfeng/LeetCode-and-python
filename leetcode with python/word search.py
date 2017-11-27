# -*- coding:utf-8 -*-
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if word == "": return True
        if len(board) == 0: return False
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[0] * len(board[0]) for i in range(0, len(board))]

        def dfs(board, visited, word, index, startx, starty):
            # if word[index] != board[startx][starty]: return False
            if index == len(word) - 1: return True
            for direction in directions:
                newx, newy = startx + direction[0], starty + direction[1]
                if newx >= 0 and newx < len(board) and newy >= 0 and newy < len(board[0]) \
                        and visited[newx][newy] == 0:
                    visited[newx][newy] = 1
                    if dfs(board, visited, word, index + 1, newx, newy): return True
                    visited[newx][newy] = 0
            return False

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                visited[i][j] = 1
                if dfs(board, visited, word, 0, i, j):
                    return True
                visited[i][j] = 0
        return False


s = Solution()
board = [
        ["ABCE"],
        ["SFCS"],
        ["ADEE"]
    ]
word = "SEE"
print(s.exist(board, word))