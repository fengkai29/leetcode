class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = [0]*len(ops)
        for i in range(len(ops)):

            flag = 1
            try:
                int(ops[i])
            except:
                flag = 0
            if flag:
                res[i] = res[i]+int(ops[i])
            else:
                if ops[i] == '+':
                    res[i] = res[i-1]+res[i-2]
                if ops[i] == 'C':
                    del res[i]
                    del res[i-1]

                    res.insert(0,0)
                    res.insert(0,0)
                if ops[i] == 'D':
                    res[i] = res[i-1]*2
        return sum(res)

s = ["36","28","70","65","C","+","33","-46","84","C"]
print(Solution().calPoints(s))