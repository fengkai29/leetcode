class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)<=1:
            return True
        res = [0]*len(nums)
        res[0] = 1
        index = 0
        count = 0
        while res[index] > 0:
              for i in range(nums[index]):
                  if index+i+1 < len(nums):
                      res[index+i+1] = 1
                  else:
                      return True
              if index < len(nums)-1:
                index += 1
              else:
                  count = 1
                  break
        if count:
            return True
        else:
            return False


num = [5,9,3,2,1,0,2,3,3,1,0,0]
m = Solution().canJump(num)
print(m)