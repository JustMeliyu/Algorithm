# -*- coding: utf-8 -*-
"""有这样一道智力题：“某商店规定：三个空汽水瓶可以换一瓶汽水。小张手上有十个空汽水瓶，她最多可以换多少瓶汽水喝？
”答案是5瓶，方法如下：先用9个空瓶子换3瓶汽水，喝掉3瓶满的，喝完以后4个空瓶子，用3个再换一瓶，喝掉这瓶满的，
这时候剩2个空瓶子。然后你让老板先借给你一瓶汽水，喝掉这瓶满的，喝完以后用3个空瓶子换一瓶满的还给老板。
如果小张手上有n个空汽水瓶，最多可以换多少瓶汽水喝？"""


class Solution:
    def drink(self, num: int):
        if num == 2:
            return 1
        if num < 2:
            return 0
        i = num // 3
        j = num % 3
        return i + self.drink(i + j)


if __name__ == '__main__':
    import sys
    s = Solution()
    for v in sys.stdin.readlines():
        if v == 0:
            break
        print(s.drink(int(v.strip("\n"))))
    for line in sys.stdin:
        a = line.split()
        print(int(a[0]) + int(a[1]))
