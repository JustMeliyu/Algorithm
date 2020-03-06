# -*- coding: utf-8 -*-

"""
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
https://leetcode-cn.com/problems/longest-palindromic-substring/
示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
"""
from tools.common import get_func_time


class Solution(object):
    """
    P(i, j) = (P(i+1,j-1) and S[i] == S[j])
    P(i, i+1) = (S[i] == S[j])
    """

    def is_palindrome(self, s: str):
        l = len(s)
        for i in range(int(l / 2)):
            if s[i] != s[l - i - 1]:
                return False
        return True

    @classmethod
    def is_palindrome2(cls, s: str):
        pass

    @get_func_time
    def longestPalindrome(self, s: str):
        # 暴力解法
        l = len(s)
        max_len = 0
        max_str = None
        for i in range(l):
            for j in range(i + 1, l):
                if self.is_palindrome(s[i:j + 1]) and len(s[i:j + 1]) > max_len:
                    max_len = len(s[i:j + 1])
                    max_str = s[i:j + 1]

        return max_len, max_str

    @get_func_time
    def longestPalindrome2(self, s: str):
        re = {}
        l = len(s)
        if l in (0, 1):
            return l, s
        elif l == 2:
            return l, s if s[0] == s[1] else 1, s[0]

        max_len = 0
        max_str = None

        for i in range(1, l - 1):
            k = l - i if l - i < i else i
            re[(i, i)] = True
            for j in range(1, k + 1):
                re[(i - j, i + j)] = (re[(i - j + 1, i + j - 1)] and s[i - j] == s[i + j])
                if re[(i - j, i + j)] and 2*j+1 > max_len:
                    max_len = 2*j+1
                    max_str = s[i-j:i+j+1]

        return max_str


if __name__ == '__main__':
    st = Solution()
    # sss = "babadsdgklxdfsioweruiotxcbnzvewituotgnmfdskjweriotuierturseopgbvzxcvbxcmviosuf"
    sss = "babad"
    # print(st.longestPalindrome(sss))
    print(st.longestPalindrome2(sss))
