# 设计一个算法，判断玩家是否赢了井字游戏。输入是一个 N x N 的数组棋盘，由字符" "，"X"和"O"组成，其中字符" "代表一个空位。
#
# 以下是井字游戏的规则：
#
# 玩家轮流将字符放入空位（" "）中。
# 第一个玩家总是放字符"O"，且第二个玩家总是放字符"X"。
# "X"和"O"只允许放置在空位中，不允许对已放有字符的位置进行填充。
# 当有N个相同（且非空）的字符填充任何行、列或对角线时，游戏结束，对应该字符的玩家获胜。
# 当所有位置非空时，也算为游戏结束。
# 如果游戏结束，玩家不允许再放置字符。
# 如果游戏存在获胜者，就返回该游戏的获胜者使用的字符（"X"或"O"）；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。
#
# 示例 1：
#
# 输入： board = ["O X"," XO","X O"]
# 输出： "X"
# 示例 2：
#
# 输入： board = ["OOX","XXO","OXO"]
# 输出： "Draw"
# 解释： 没有玩家获胜且不存在空位
# 示例 3：
#
# 输入： board = ["OOX","XXO","OX "]
# 输出： "Pending"
# 解释： 没有玩家获胜且仍存在空位

"""
本题的关键就在于是python3 里面any的使用
any() 函数用于判断给定的可迭代参数 iterable 是否全部为 False，则返回 False，如果有一个为 True，则返回 True。
元素除了是 0、空、FALSE 外都算 TRUE。
传入的参数可以是迭代的元组或者列表
"""
class Solution(object):
    def tictactoe(self, board):##borad 是一个多元的列表
        n=len(board)#也就是要生成的数组的N

        def check(c):#传入获胜方的输入
            s=c*n#用于判定整行或者整列,比如输入x,则为xxx
            return any((any(row==s for row in board),any(col==s for col in map(''.join,zip(*board))),
                        all(board[i][i]==c for i in range(n)),
                        all(board[i][n-i-1]==c for i in range(n))
                        ))##返回的是一个boolean的事情，学会取出一列的方法，另外学会any和all函数的使用

        if check('X'):##如果条件为真
            return 'X'
        if check('O'):
            return 'O'
        if ' ' in ''.join(board):
            return 'Pending'
        return 'Draw'

def main():
    board=[['X','O','X'],['O','X','O'],['X','O','X']]
    s=Solution()
    print(s.tictactoe(board))


if __name__=="__main__":
    main()


