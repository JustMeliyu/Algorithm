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


class Solution(object):
    def longestPalindrome(self, s):
        """
        P(i, j) = (P(i+1,j-1) and S[i] == S[j])
        P(i, i+1) = (S[i] == S[j])
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return len(s)
        re = 0
        for i, _s in enumerate(s):
            j = i
            while j > 0:

