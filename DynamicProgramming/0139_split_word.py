# -*-coding:utf-8-*- 

"""
Author: Road36
Date: 2020-04-13
Describe:
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
链接：https://leetcode-cn.com/problems/word-break
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        最简单的实现方法是用递归和回溯。为了找到解，我们可以检查字典单词中每一个单词的可能前缀，如果在字典中出现过，
        那么去掉这个前缀后剩余部分回归调用。同时，如果某次函数调用中发现整个字符串都已经被拆分且在字典中出现过了，
        函数就返回 true 。
        :param s:
        :param wordDict:
        :return:
        """
        def word_break(s, word_dict, start):
            if start == len(s):
                return True
            for end in range(start+1, len(s) + 1):
                a = s[start:end]
                if a in word_dict and word_break(s, word_dict, end):
                    return True
            return False
        return word_break(s, wordDict, 0)

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(wordDict) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and (s[j:i] in wordDict):
                    dp[i] = True
        return dp[-1]


if __name__ == '__main__':
    st = Solution()
    char = "piepiepend"
    # char = "leetcode"
    word_dict = ['pie', 'piep', 'end']
    # word_dict = ['leet', 'code']
    print(st.wordBreak2(char, word_dict))
