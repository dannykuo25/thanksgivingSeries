class Solution:
    def tictactoe(self, moves):
        grid = [[' ' for _ in range(3)] for _ in range(3)]
        n = len(moves)
        for i in range(n):
            # # put
            # if i % 2 == 0: # A's turn
            #     grid[moves[i][0]][moves[i][1]] = 'X'
            # else: # B's turn
            #     grid[moves[i][0]][moves[i][1]] = 'O'
            # check
            whoWin = self.checkWin(grid, moves[i][0], moves[i][1], i % 2)
            # print(whoWin)
            # print(grid)
            if whoWin == 'A':
                return 'A'
            elif whoWin == 'B':
                return 'B'
        if n == 9:
            return 'Draw'
        else:
            return 'Pending'
        
    def checkWin(self, grid, i, j, turn):
        
        if turn == 0: # A's turn
            grid[i][j] = 'X'
            # horizontal
            if self.horizontalCheck(grid, i, j, 'X') == 3 or self.verticalCheck(grid, i, j, 'X') == 3 or self.slopeCheck(grid, i, j, 'X') == 3:
                return 'A'
            
        else:
            grid[i][j] = 'O'
            if self.horizontalCheck(grid, i, j, 'O') == 3 or self.verticalCheck(grid, i, j, 'O') == 3 or self.slopeCheck(grid, i, j, 'O') == 3:
                return 'B'
        
        return 'Other'
    
    def horizontalCheck(self, grid, i, j, XO):
        cnt = 1
        k = j
        while k > 0:
            k -= 1
            if grid[i][k] == XO:
                cnt += 1
        k = j
        while k < 2:
            k += 1
            if grid[i][k] == XO:
                cnt += 1
        return cnt
                
    def verticalCheck(self, grid, i, j, XO):
        cnt = 1
        k = i
        while k > 0:
            k -= 1
            if grid[k][j] == XO:
                cnt += 1
        k = i
        while k < 2:
            k += 1
            if grid[k][j] == XO:
                cnt += 1
        return cnt
    
    def slopeCheck(self, grid, i, j, XO):
        cnt = 1
        left, right = 0, 0
        if (i == 0 and j == 0) or (i == 1 and j == 1) or (i == 2 and j == 2):
            left = self.leftSlope(grid, i, j, XO)
            # print(left, 'left')
        if (i == 0 and j == 2) or (i == 1 and j == 1) or (i == 2 and j == 0):
            right = self.rightSlope(grid, i, j, XO)
            # print(right, 'right')
        return cnt + max(left, right)
    
    def leftSlope(self, grid, i, j, XO):
        ret = 0
        k = i
        while k > 0:
            k -= 1
            if grid[k][k] == XO:
                ret += 1
        k = i
        while k < 2:
            k += 1
            if grid[k][k] == XO:
                ret += 1
        return ret
    
    def rightSlope(self, grid, i, j, XO):
        ret = 0
        k, l = i, j
        while k > 0:
            k -= 1
            l += 1
            if grid[k][l] == XO:
                ret += 1
        k, l = i, j
        while l > 0:
            k += 1
            l -= 1
            if grid[k][l] == XO:
                ret += 1
        return ret
            
Input = [[0,2],[1,0],[2,2],[1,2],[2,0],[0,0],[0,1],[2,1],[1,1]]


# Tic-tac-toe is played by two players A and B on a 3 x 3 grid.

# Here are the rules of Tic-Tac-Toe:

# Players take turns placing characters into empty squares (" ").
# The first player A always places "X" characters, while the second player B always places "O" characters.
# "X" and "O" characters are always placed into empty squares, never on filled ones.
# The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given an array moves where each element is another array of size 2 corresponding to the row and column of the grid where they mark their respective character in the order in which A and B play.

# Return the winner of the game if it exists (A or B), in case the game ends in a draw return "Draw", if there are still movements to play return "Pending".

# You can assume that moves is valid (It follows the rules of Tic-Tac-Toe), the grid is initially empty and A will play first.



# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# Explanation: "A" wins, he always plays first.
# "X  "    "X  "    "X  "    "X  "    "X  "
# "   " -> "   " -> " X " -> " X " -> " X "
# "   "    "O  "    "O  "    "OO "    "OOX"

# Example 2:

# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# Explanation: "B" wins.
# "X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
# "   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
# "   "    "   "    "   "    "   "    "   "    "O  "

# Example 3:

# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.
# "XXO"
# "OOX"
# "XOX"

# Example 4:

# Input: moves = [[0,0],[1,1]]
# Output: "Pending"
# Explanation: The game has not finished yet.
# "X  "
# " O "
# "   "

# Constraints:

# 1 <= moves.length <= 9
# moves[i].length == 2
# 0 <= moves[i][j] <= 2
# There are no repeated elements on moves.
# moves follow the rules of tic tac toe.

