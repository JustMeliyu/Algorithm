# -*-coding:utf-8-*-
"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
"""


class Solution:
    def reverse(self, x: int) -> int:
        if -2 ** 31 > x or x > (2 ** 31 - 1):
            return 0

        def _reverse(_x: int) -> int:
            a = int(str(_x)[::-1])
            return 0 if a < -2 ** 31 or a > 2 ** 31 - 1 else a

        if x < 0:
            return -_reverse(-x)
        else:
            return _reverse(x)


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(1534236469))
