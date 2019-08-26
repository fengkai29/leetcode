class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        flag1 = 0
        flag2 = 0
        for i in range(len(moves)):
            if moves[i] == 'U':
                flag1 = flag1 + 1
            if moves[i] == 'D':
                flag1 = flag1 - 1
            if moves[i] == 'L':
                flag2 = flag2 + 1
            if moves[i] == 'R':
                flag2 = flag2 - 1
        if flag1 == 0 and flag2 == 0:
            return True
        else:
            return False

#return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')