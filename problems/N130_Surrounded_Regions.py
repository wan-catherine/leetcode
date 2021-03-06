class Solution(object):
    def solve_before(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.board = board
        if not self.board or not len(self.board) or not len(self.board[0]):
            return
        self.row_len = len(self.board)
        self.col_len = len(self.board[0])

        visited = [[0] * self.col_len for _ in range(self.row_len)]
        stack = []
        for i in range(self.row_len):
            for j in range(self.col_len):
                if self.board[i][j] == 'X' or visited[i][j] == 1:
                    continue
                if not stack:
                    stack.append((i,j))
                    is_change = True
                    o_array = []
                while stack:
                    row, col = stack.pop()
                    if visited[row][col]:
                        continue
                    visited[row][col] = 1
                    o_array.append((row, col))
                    if is_change and self.is_border_O(row, col):
                        is_change = False
                    if row >= 1 and self.board[row-1][col] == 'O':
                        stack.append((row-1, col))
                    if col >= 1 and self.board[row][col-1] == 'O':
                        stack.append((row, col-1))
                    if row < self.row_len - 1 and self.board[row+1][col] == 'O':
                        stack.append((row+1, col))
                    if col < self.col_len -1 and self.board[row][col+1] == 'O':
                        stack.append((row, col+1))
                if is_change:
                    for t in o_array:
                        self.board[t[0]][t[1]] = 'X'
        return board

    def is_border_O(self, row, col):
        if self.board[row][col] == 'O':
            if row == 0 or col == 0:
                return True
            if row == self.row_len - 1 or col == self.col_len - 1:
                return True
        return False

    def solve(self, board):
        if not board or not board[0]:
            return
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        stack = []
        update = [['p'] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                if (row > 0 and row < rows - 1) and (col > 0 and col < cols - 1):
                    continue
                if board[row][col] != 'O' or update[row][col] == '1':
                    continue
                stack.append((row, col))
                while stack:
                    pos = stack.pop()
                    update[pos[0]][pos[1]] = '1'
                    for i, j in directions:
                        new_row, new_col = pos[0] + i, pos[1] + j
                        if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                            continue
                        if update[new_row][new_col] != '1' and board[new_row][new_col] == 'O':
                            stack.append((new_row, new_col))
                            update[new_row][new_col] == '1'

        for row in range(rows):
            for col in range(cols):
                if update[row][col] != '1' and board[row][col] == 'O':
                    board[row][col] = 'X'

        return board

