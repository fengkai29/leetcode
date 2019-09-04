class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dic = {'5':0,'10':0}
        i = 0
        while i < len(bills):
            if bills[i] == 5:
                dic['5'] = dic['5']+1
            if bills[i] == 10:
                if dic['5'] >0:
                    dic['5'] = dic['5'] - 1
                    dic['10'] = dic['10'] + 1
                else:
                    return False
            if bills[i] == 20:
                if dic['10']>0 and dic['5']>0:
                    dic['10'] = dic['10'] - 1
                    dic['5'] = dic['5'] - 1
                elif dic['10'] == 0 and dic['5']>=3:
                    dic['5'] = dic['5'] - 3
                else:
                    return False
            i = i + 1
        return True
