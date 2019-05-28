# -*- coding: utf-8 -*- 

__author__ = "Road36"
__date__ = "19-5-28"

"""
Describe:
给定一个字符串 S，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转
"""


class Solution:
    def reverseOnlyLetters(self, varchar: str) -> str:
        not_str_info = {}
        new_s = ""
        for i in range(len(varchar)):
            if not self.is_alphabet(varchar[i]):
                not_str_info[i] = varchar[i]
            else:
                new_s = varchar[i] + new_s
        for k, v in not_str_info.items():
            new_s = new_s[:k] + v + new_s[k:]
        return new_s

    @classmethod
    def is_alphabet(cls, uchar):
        """判断一个unicode是否是英文字母"""
        return (u'\u0041' <= uchar <= u'\u005a') or (u'\u0061' <= uchar <= u'\u007a')


if __name__ == '__main__':
    s = Solution()
    a = "Test1ng-Leet=code-Q!"
    b = s.reverseOnlyLetters(a)
    print(b)
