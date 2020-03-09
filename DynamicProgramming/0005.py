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

    def is_palindrome(self, s):
        l = len(s)
        for i in range(int(l / 2)):
            if s[i] != s[l - i - 1]:
                return False
        return True

    @classmethod
    def is_palindrome2(cls, s):
        pass

    @get_func_time
    def longestPalindrome3(self, s: str) -> str:
        # 暴力解法
        l = len(s)
        max_len = 0
        max_str = None
        for i in range(l):
            for j in range(i + 1, l):
                if self.is_palindrome(s[i:j + 1]) and len(s[i:j + 1]) > max_len:
                    max_len = len(s[i:j + 1])
                    max_str = s[i:j + 1]

        return max_str

    @get_func_time
    def longestPalindrome2(self, s: str) -> str:
        l = len(s)
        if l in (0, 1):
            return s
        elif l == 2:
            return s if s[0] == s[1] else s[0]

        max_len = 1
        max_str = s[0]

        for i in range(l - 1):
            k = 0
            while i - k >= 0 and i + k < l and s[i-k] == s[i+k]:
                if 2*k + 1 > max_len:
                    max_len = 2*k + 1
                    max_str = s[i - k:i + k + 1]
                k += 1

            k = 0
            if i + 1 > l or s[i] != s[i + 1]:
                continue

            while i - k >= 0 and i + k + 1 < l and s[i-k] == s[i+k+1]:
                if 2*k + 2 > max_len:
                    max_len = 2*k + 2
                    max_str = s[i - k:i + k + 2]
                k += 1
        return max_str

    @get_func_time
    def longestPalindrome(self, s: str) -> str:
        """pass all case by myself"""
        re = {}
        l = len(s)
        if l in (0, 1):
            return s
        max_len = 1
        max_str = s[0]
        for i in range(1, l + 1):
            for j in range(l):
                end = j + i - 1
                if end > l - 1:
                    break

                if i == 1:
                    re[(j, end)] = True
                elif i == 2:
                    re[(j, end)] = (s[j] == s[end])
                else:
                    re[(j, end)] = (re[(j + 1, end - 1)] and (s[j] == s[end]))

                if re[(j, end)] and i > max_len:
                    max_len = i
                    max_str = s[j:end+1]
        return max_str

    def longestPalindrome4(self, s: str) -> str:
        """best code on leetcode"""
        if len(s) < 2 or s == s[::-1]:
            return s

        max_length = 1
        even_left = 0
        even_medium = 0

        for i in range(len(s) - 1):
            if i - even_left >= 0 and s[i - even_left] == s[i + 1]:
                substring = s[i - even_left: i + 2]
                if substring == substring[::-1]:
                    even_medium = i
                    max_length = even_left + 2
                    even_left += 2

        odd_medium = 0
        half = (max_length + 1) // 2
        odd_left = half

        for j in range(half, len(s) - half):
            if j - odd_left >= 0 and s[j - odd_left] == s[j + half]:
                substring = s[j - odd_left: j + half + 1]
                if substring == substring[::-1]:
                    odd_medium = j
                    max_length = odd_left + half + 1
                    odd_left += 2

        if max_length % 2 == 0:
            return s[even_medium - even_left + 2: even_medium + 2]
        else:
            return s[odd_medium - odd_left + 2:odd_medium + half + 1]


if __name__ == '__main__':
    st = Solution()
    sss = "whdqcudjpisufnrtsyupwtnnbsvfptrcgvobbjglmpynebblpigaflpbezjvjgbmofejyjssdhbgghgrhzuplbeptpaecfdanhlylgusptlgobkqnulxvnwuzwauewcplnvcwowmbxxnhsdmgxtvbfgnuqdpxennqglgmspbagvmjcmzmbsuacxlqfxjggrwsnbblnnwisvmpwwhomyjylbtedzrptejjsaiqzprnadkjxeqfdpkddmbzokkegtypxaafodjdwirynzurzkjzrkufsokhcdkajwmqvhcbzcnysrbsfxhfvtodqabvbuosxtonbpmgoemcgkudandrioncjigbyizekiakmrfjvezuzddjxqyevyenuebfwugqelxwpirsoyixowcmtgosuggrkdciehktojageynqkazsqxraimeopcsjxcdtzhlbvtlvzytgblwkmbfwmggrkpioeofkrmfdgfwknrbaimhefpzckrzwdvddhdqujffwvtvfyjlimkljrsnnhudyejcrtrwvtsbkxaplchgbikscfcbhovlepdojmqybzhbiionyjxqsmquehkhzdiawfxunguhqhkxqdiiwsbuhosebxrpcstpklukjcsnnzpbylzaoyrmyjatuovmaqiwfdfwyhugbeehdzeozdrvcvghekusiahfxhlzclhbegdnvkzeoafodnqbtanfwixjzirnoaiqamjgkcapeopbzbgtxsjhqurbpbuduqjziznblrhxbydxsmtjdfeepntijqpkuwmqezkhnkwbvwgnkxmkyhlbfuwaslmjzlhocsgtoujabbexvxweigplmlewumcone"
    # sss = "babad"
    # sss = "cbbd"
    # print(st.longestPalindrome(sss))
    print(st.longestPalindrome2(sss))
