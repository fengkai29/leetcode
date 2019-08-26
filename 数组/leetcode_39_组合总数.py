class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        for i, n in enumerate(candidates):
            if n == target:
                result.append([n])
            elif n < target:
                p_result = self.combinationSum(candidates[i:], target - n)
                for p_n in p_result:
                    p_n.append(n)
                    result.append(p_n)
        return result

