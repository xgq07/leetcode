import unittest
# 斐波那契数列
def fib(n):
    # 由前往后推
    a = 1
    b = 1
    if n <= 2:
        print('fab({})={}'.format(n, b))
        return 1
    for i in range(n - 2):
        print(a, b)
        a, b = b, a + b
    print('fab({})={}'.format(n, b))
    return b

def fib2(n):
    a=0
    b=1
    for i in range(n):
        b=a+b
        a,b=b,a
    return b



from typing import List
class Massage(unittest.TestCase):
    def massage(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        
        dp0, dp1 = 0, nums[0]
        for i in range(1, n):
            tdp0 = max(dp0, dp1)   # 计算 dp[i][0]
            tdp1 = dp0 + nums[i]   # 计算 dp[i][1]
            dp0, dp1 = tdp0, tdp1

        return max(dp0, dp1)

    def massage2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) < 3:
            return max(nums)
        f, s = nums[0], nums[1]
        for i in range(2, len(nums)):
            t = max(f+nums[i], s)
            f = max(f, s)
            s = t
        return t

    def test_massage(self):
        assert self.massage([1, 2, 3, 1]) == 4          # 1+3
       # assert self.massage([2, 7, 9, 3, 1]) == 12      # 2+9+1
       # assert self.massage([2, 1, 4, 5, 3, 1, 1, 3]) == 12 # 2+4+3+3



if __name__ == "__main__":
    #p = [fib2(i) for i in range(1,10)]
    #print(p)
    unittest.main()
