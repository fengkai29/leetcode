class Solution(object):
    def __init__(self):
        self.dec = [(0,1),(1,0),(0,-1),(-1,0)]

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if board == []:
            return []
        w = len(board[0])
        h = len(board)
        for i in range(h):
            if board[i][0] == 'O':
                board[i][0] == 'B'
                self.dfs(board,i,0,w,h)
        for i in range(h):
            if board[i][-1] == 'O':
                board[i][-1] == 'B'
                self.dfs(board,i,w-1,w,h)
        for i in range(w):
            if board[0][i] == 'O':
                board[0][i] == 'B'
                self.dfs(board,0,i,w,h)
        for i in range(w):
            if board[-1][i] == 'O':
                board[-1][i] == 'B'
                self.dfs(board,h-1,i,w,h)
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(h):
            for j in range(w):
                if board[i][j] == 'B':
                    board[i][j] = 'O'

    def dfs(self,board,i,j,w,h):
        board[i][j] = 'B'
        for dec in self.dec:
            new_i = i + dec[0]
            new_j = j + dec[1]
            if 0<= new_i < h and 0 <= new_j <w and board[new_i][new_j] == 'O':
                self.dfs(board,new_i,new_j,w,h)