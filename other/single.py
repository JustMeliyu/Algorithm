# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 2020-03-28
Describe:
__new__ 在对象创建之前创建一个对象并将该对象传递给 init
__init__ 在对象创建后对对象进行初始化
"""

import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_isinstance'):
            with Singleton._instance_lock:  # 防止多线程时错误
                if not hasattr(cls, '_instance'):
                    Singleton._instance = super().__new__(cls)
        return Singleton._instance


if __name__ == '__main__':
    obj1 = Singleton()
    obj2 = Singleton()
    print(id(obj1))
    print(id(obj2))