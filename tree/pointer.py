# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-04-10
Describe:
快慢指针，求环
"""

from tools.construction import ChainNode
from typing import List


class Pointer:
    """类似下面的思路，我们还可以让快指针一次前进两步，慢指针一次前进一步，当快指针到达链表尽头时，慢指针就处于链表的中间位置。"""

    def has_cycle(self, chain: ChainNode) -> bool:
        """
        一个块指针，一个慢指针，当快慢指针相遇时，说明有环; 当块指针next为None时，说明不为环；
        """
        fast = slow = chain
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return False
        return True

    def detect_cycle(self, chain: ChainNode) -> ChainNode:
        """
        假设chain是环，求环开始的地方。
        当快慢指针相遇，慢指针走了k，则块指针一定走了2k，则环的距离为k;
        假设相遇点距离环起点距离为m，则head与相遇点距离为k - m，刚好从相遇点再走k - m步，刚好到达环起点
        """
        fast = slow = chain
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break

        slow = chain
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

    def left_right_pointer(self, nums: List[int], target: int):
        """
        左右指针在数组中实际是指两个索引值，一般初始化为 left = 0, right = nums.length - 1 。
        从一个数组里，找出两个值，合为指定值
        """
        start = 0
        end = len(nums) - 1

        while start < end:
            tmp_sum = nums[start] + nums[end]
            if tmp_sum == target:
                return start, end
            if tmp_sum > target:
                end -= 1
            else:
                start += 1
        return None, None


if __name__ == '__main__':
    s = Pointer()
    print(s.left_right_pointer([2, 7, 11, 15], 9))
