# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-03-28
Describe:
死锁
在多线程中，死锁的线程，多半是因为一个线程需要获取多个锁造成的
"""

import time
import threading
from contextlib import contextmanager


class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id
        self.balance = balance
        self.lock = lock

    def withdraw(self, amount):
        print(self.id, 'withraw')
        self.balance -= amount

    def deposit(self, amount):
        print(self.id, 'deposit')
        self.balance += amount


def transfer(_from, to, amount):
    # 可能会形成死锁
    if _from.lock.acquire():  # 锁住自己的账户
        _from.withdraw(amount)
        time.sleep(1)  # 让交易时间变长，2个交易线程时间上重叠，有足够时间来产生死锁
        print('wait for lock...')
        if to.lock.acquire():  # 锁住对方的账户
            to.deposit(amount)
            to.lock.release()
        _from.lock.release()
    print('finish...')


def transfer2(_from, to, amount):
    if _from.lock.acquire():  # 锁住自己的账户
        _from.withdraw(amount)
        time.sleep(1)  # 让交易时间变长，2个交易线程时间上重叠，有足够时间来产生死锁
        print('wait for lock...')
        if to.lock.acquire(timeout=1):  # 锁住对方的账户，超时
            to.deposit(amount)
            to.lock.release()
        else:
            print('timeout\n')  # 放置死锁
            _from.deposit(amount)
        _from.lock.release()
    print('finish...')


if __name__ == '__main__':
    a = Account('a', 1000, threading.Lock())
    b = Account('b', 1000, threading.Lock())
    # a = Account('a', 1000, threading.RLock())
    # b = Account('b', 1000, threading.RLock())
    threading.Thread(target=transfer, args=(a, b, 100)).start()
    threading.Thread(target=transfer, args=(b, a, 200)).start()
    threading.Thread(target=transfer2, args=(a, b, 100)).start()
    threading.Thread(target=transfer2, args=(b, a, 200)).start()
    time.sleep(3)
    print(a.balance)
    print(b.balance)
