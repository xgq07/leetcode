from typing import List

class Solution:
    def __init__(self):
        super().__init__()
   
    # 此方法超出时间限制
    def minIncrementForUnique(self, A: List[int]) -> int:        
        #逐一往set中增加
        #判断增加1后set中是否增加
        sset = set()
        moveTimes = 0
        for a in A:
            expect_len = len(sset) + 1
            sset.add(a)
            sset_len = len(sset)
            toadd = a
            while sset_len != expect_len:
                toadd = toadd + 1
                sset.add(toadd)
                moveTimes += 1
                sset_len = len(sset)
        
        return moveTimes
       

    # def isSetEqualLen(self) -> bool:
    #     if self.sset 
    #     return True

if __name__ == "__main__":
    s = Solution()
    print(s.minIncrementForUnique([1,2,2])) #1
    print(s.minIncrementForUnique([3,2,1,2,1,7])) #1
