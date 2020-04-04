from typing import List
# 70. 爬楼梯
# https://leetcode-cn.com/problems/climbing-stairs/
class Solution:
    def __init__(self):
        super().__init__()
        self.dic = {1:1, 2:2}

    def climbStairs(self, n: int) -> int:
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]


# 22. 括号生成
# https://leetcode-cn.com/problems/generate-parentheses/solution/gua-hao-sheng-cheng-by-leetcode/
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def generate(left , right, n, s):
            # terminator
            if left == n and right == n:
                res.append(s)
                return
            # process
            # drill down
            if left < n:
                generate(left + 1, right , n, s + "(")
            
            if left > right:
                generate(left, right + 1, n, s + ")")
            # reverse states
        
        generate(0, 0, n, "")
        return res


s = Solution()
print(s.climbStairs(3))
print(s.generateParenthesis(3))


