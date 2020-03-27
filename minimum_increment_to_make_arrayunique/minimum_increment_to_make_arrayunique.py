from typing import List

class Solution:
    def __init__(self):
        super().__init__()
   
    # 此方法超出时间限制
    # def minIncrementForUnique(self, A: List[int]) -> int:        
    #     #逐一往set中增加
    #     #判断增加1后set中是否增加
    #     sset = set()
    #     moveTimes = 0
    #     for a in A:
    #         expect_len = len(sset) + 1
    #         sset.add(a)
    #         sset_len = len(sset)
    #         toadd = a
    #         while sset_len != expect_len:
    #             toadd = toadd + 1
    #             sset.add(toadd)
    #             moveTimes += 1
    #             sset_len = len(sset)
        
    #     return moveTimes

    # 变了数组的值
    # def minIncrementForUnique(self, A: List[int]) -> int:
    #     A.sort()
    #     res = 0
    #     for i in range(len(A)-1):
    #         if A[i] >= A[i+1]:
    #             # 存下 A[i+1] 后续用
    #             temp = A[i+1]
    #             # 给后面的 + 1
    #             A[i+1] = A[i]+1      
    #             # (原来数 - 后面数(temp) + 1) ＝ 如（１，２，２，２） ＝ A[i]{2} - A[i+1]{2} + 1 = 1   
    #                                     # = (1, 2, 3, 2)  = A[i]{3} - A[i+1]{2} + 1 = 2
    #             # res += (A[i]-temp+1)

    #             # (增加后的数 - 原来的值) = 要增加的次数
    #             res +=(A[i + 1] - temp)
    #     return res


    # Sort the input array.
    # Compared with previous number,
    # the current number need to be at least prev + 1.
    # def minIncrementForUnique(self, A: List[int]) -> int:
    #     # res  与 need 初始
    #     res = need = 0
    #     for i in sorted(A):
    #         res += max(need - i, 0)
    #         need = max(need + 1, i + 1)
    #     return res
    
    def minIncrementForUnique(self, A: List[int]) -> int:
        A.sort()
        res = 0
        for i in range(len(A)-1):
            curri = i
            nexti = i + 1
            if A[curri] >= A[nexti]:
                temp = A[nexti]
                A[nexti] = A[curri] + 1
                res += A[nexti] - temp
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.minIncrementForUnique([1,2,2])) #1
    print(s.minIncrementForUnique([3,2,1,2,1,7])) #6
