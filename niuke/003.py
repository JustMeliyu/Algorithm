# -*- coding: utf-8 -*-

import sys
from typing import List


class Solution:
    def sort_cd(self, cd: List):
        re = dict()
        for j in cd:
            if j[-1] == "M":
                k = int(j[:-1])
            elif j[-1] == "G":
                k = int(j[:-1]) * 1000
            else:
                k = int(j[:-1]) * 1000 * 1000
            if k in re.keys():
                re[k]['count'] += 1
            else:
                re[k] = {"value": j, "count": 1}

        a = sorted(re.keys())
        for j in a:
            for z in range(re[j]['count']):
                print(re[j]['value'])


if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    r = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        r.append(line)
    s = Solution()
    s.sort_cd(r)
