class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == flowerbed.count(0):
            a = (len(flowerbed)+1)/2
            if a>=n:
                return True
            else:
                return False
        i = 0
        count = 0
        flag = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                break
            count = count + 1
            i = i + 1
        m = i + 1
        flag = flag + int(count/2)
        i = len(flowerbed)-1
        count = 0
        while i > -1:
            if flowerbed[i] == 1:
                break
            count = count + 1
            i = i - 1
        flag = flag + int(count / 2)
        k = i + 1
        count = 0
        while m < k:
            if flowerbed[m] == 0:
                count +=1
            if flowerbed[m] == 1:
                if count == 0 or count == 1 or count ==2:
                    flag = flag
                    count = 0
                else:
                    flag = flag + int((count+1)/2)-1
                    count = 0
            m = m + 1
        if flag>=n:
            return True
        else:
            False

a = [1,0,1,0,1,0,1]
k = 1
print(Solution().canPlaceFlowers(a,k))