class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int):
        for i in range(cheeseSlices + 1):
            if i * 2 + (cheeseSlices - i) * 4 == tomatoSlices:
                return [cheeseSlices - i, i]
        return []

class Solution2:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int):
        t = tomatoSlices
        c = cheeseSlices
        return [t // 2 - c, c * 2 - t // 2] if t % 2 == 0 and c * 2 <= t <= c * 4 else []

# Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:

# Jumbo Burger: 4 tomato slices and 1 cheese slice.
# Small Burger: 2 Tomato slices and 1 cheese slice.
# Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

# Example 1:

# Input: tomatoSlices = 16, cheeseSlices = 7
# Output: [1,6]
# Explantion: To make one jumbo burger and 6 small burgers we need 4*1 + 2*6 = 16 tomato and 1 + 6 = 7 cheese. There will be no remaining ingredients.
# Example 2:

# Input: tomatoSlices = 17, cheeseSlices = 4
# Output: []
# Explantion: There will be no way to use all ingredients to make small and jumbo burgers.
# Example 3:

# Input: tomatoSlices = 4, cheeseSlices = 17
# Output: []
# Explantion: Making 1 jumbo burger there will be 16 cheese remaining and making 2 small burgers there will be 15 cheese remaining.
# Example 4:

# Input: tomatoSlices = 0, cheeseSlices = 0
# Output: [0,0]
# Example 5:

# Input: tomatoSlices = 2, cheeseSlices = 1
# Output: [0,1]
 

# Constraints:

# 0 <= tomatoSlices <= 10^7
# 0 <= cheeseSlices <= 10^7