class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people == []:
            return
        people = sorted(people,key=lambda x:(-x[0],x[1]))
        ls = []
        for m in people:
            ls.insert(m[1],m)
        return ls