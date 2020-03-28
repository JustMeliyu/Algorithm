# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-03-28
Describe:
说起约德尔人的未来，黑默丁格曾经提出了一个约德尔测试，将约德尔人的历史的每个阶段都用一个字符表达出来。(包括可写字符,不包括空格。)。
然后将这个字符串转化为一个01串。转化规则是如果这个字符如果是字母或者数字，这个字符变为1,其它变为0。
然后将这个01串和黑默丁格观测星空得到的01串做比较，得到一个相似率。相似率越高,则约德尔的未来越光明。

输入
每组输入数据为两行，第一行为有关约德尔人历史的字符串，第二行是黑默丁格观测星空得到的字符串。
(两个字符串的长度相等,字符串长度不小于1且不超过1000。)
@!%12dgsa
010111100

输出
输出一行，在这一行输出相似率。用百分数表示。(相似率为相同字符的个数/总个数,精确到百分号小数点后两位。printf("%%");输出一个%。)
66.67%
"""


class Solution:
    def proportion(self, str1: str, str2: str) -> str:
        _l = len(str1)
        _n = 0
        for i, v in enumerate(str1):
            if v.isdigit() or v.isalpha():
                if str2[i] == '1':
                    _n += 1
            else:
                if str2[i] == '0':
                    _n += 1
        print(_n)
        return "%.02f%%" % (float(_n / _l) * 100)


if __name__ == '__main__':
    s = Solution()
    # print(Solution.is_num("1"))
    print(s.proportion('@!%12dgsa', "010111100"))
