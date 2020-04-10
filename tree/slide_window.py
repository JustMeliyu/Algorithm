# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-04-10
Describe:
https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%8A%80%E5%B7%A7.md
滑动窗口
1. 先定义两个指针，一般left=right=0，[left:right]被称为一个窗口
2. 先让right不断增大，直到找到符合条件为止
3. 让left再不断增大，直到找打不符合条件为止
4. 再让right不断增大，直到边界

抽象思想

while right < len(s):
    right += 1
    window.append(s[right])

    while valid:
        window.remove(s[left])
        left += 1
"""


class SlideWindow:
    def is_include(self, origin_str: str, match_str: str):
        """
        给两个字符串，在origin_str中，找出包含match_str所有字母的最短字符串
        origin_str = "ADOBECODEBANC" , match_str = "ABC"
        return : BANC
        """
        left = right = 0
        _l = len(origin_str)
        shortest_str = origin_str
        include = {key: 0 for key in match_str}
        while right < _l:
            if origin_str[right] in match_str:
                include[origin_str[right]] += 1
            if 0 in include.values():   # right向右滑
                right += 1
                continue

            # while 0 in include.values():    # right向右滑
            #     if origin_str[right] in match_str:
            #         include[origin_str[right]] += 1
            #     right += 1

            while 0 not in include.values():    # left向右滑
                if origin_str[left] in match_str:
                    include[origin_str[left]] -= 1
                left += 1

            # 此时[left - 1: right + 1) 包含match_str
            shortest_str = origin_str[left - 1:right + 1] if right - left + 2 < len(shortest_str) else shortest_str
            right += 1
        return shortest_str

    def repeat_str(self, origin_str: str):
        """
        给出一个字符串，求该字符串中最长无重复的字符串
        """
        left = right = 0
        _l = len(origin_str)
        longest_str = ""
        while right < _l:
            if origin_str[right] not in origin_str[left:right]:
                right += 1
                longest_str = origin_str[left:right] if right - left > len(longest_str) else longest_str
                continue

            tmp_index = origin_str[left:right].index(origin_str[right])     # 找到[left:right)中出现origin_srt[right]的地方
            left += tmp_index + 1
        return len(longest_str)


if __name__ == '__main__':
    sw = SlideWindow()
    # print(sw.is_include("ADOBECODEBANC", "ABC"))
    print(sw.repeat_str(""))
