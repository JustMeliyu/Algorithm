# -*- coding: utf-8 -*-

"""
Author: Road36
Date: 19-5-17
Describe:
"""
import simpy
import random
import numpy as np


class EmuEnvironment(simpy.Environment):
    def __init__(self):
        super().__init__()

    def prepare(self):
        pass


class Emulator:

    PROCESS = ['fetch', 'decode', 'execute', 'write_back']

    def __init__(self):
        self.current_op = None
        self.env = simpy.Environment()
        self.emu_op = None
        self.ops = [_ for _ in range(10)]
        self.pc = 0
        self.jump_pc = []
        self.current_ops = list
        self.fetch_resource = simpy.Resource(self.env)
        self.decode_resource = simpy.Resource(self.env)
        self.execute_resource = simpy.Resource(self.env)
        self.write_back_resource = simpy.Resource(self.env, 2)
        self.memory_access = simpy.Resource(self.env, 1)
        self.fetch_reactivate = self.env.event()
        self.decode_reactivate = self.env.event()
        self.execute_reactivate = self.env.event()
        self.write_back_reactivate = self.env.event()
        self.pre_three_pc = list
        self.pre_four_wheel = []
        self.pre_four_wheel_index = []
        self.cycle = 0
        self.rewrite = self.env.event()
        self.tmp = []
        self.count = 0

    @property
    def process(self):
        random.shuffle(self.PROCESS)
        return self.PROCESS

    def get_init_process(self):
        tmp = self.process.copy()
        random.shuffle(tmp)
        return tmp

    def prepare(self):
        pass

    def set_wheels(self, wheel):
        if len(self.pre_four_wheel) == 4:
            self.pop_wheels()
        self.pre_four_wheel.append(wheel)
        np.random.shuffle(self.pre_four_wheel)
        pcs = [x.pc for x in self.pre_four_wheel]
        # print("xxxxx", pcs)

    def pop_wheels(self):
        earliest_wheel = min(self.pre_four_wheel, key=lambda x: x.cycle)
        self.pre_four_wheel.remove(earliest_wheel)

    def run_op(self, pc=None):
        # self.set_wheels(EmuWheel(self.env, pc, self.cycle, self))
        # self.get_wheels()
        if len(self.pre_four_wheel) == 4:
            self.pre_four_wheel.pop(0)
        self.pre_four_wheel.append(EmuWheel(self.env, pc, self.cycle, self))
        wheels = self.pre_four_wheel.copy()
        tmp = random.randint(0, 100)
        print("--"*10, tmp, [wheel.next_process.__name__ for wheel in wheels])
        for wheel in wheels:
            self.count += 1
            # print(tmp)
            process = wheel.next_process
            yield self.env.process(process)

            # if process.__name__ == 'fetch':
            #     print("     fetch finish", process.__name__, wheel.pc)
            # elif process.__name__ == 'decode':
            #     print("     decode finish", process.__name__, wheel.pc)
            # elif process.__name__ == 'execute':
            #     print("     execute finish", process.__name__, wheel.pc)
            # else:
            #     print("     write_back finish", process.__name__, wheel.pc)
            # print("==, finish", process.__name__, wheel.pc)
            # self.rewrite.succeed()
            # self.rewrite = self.env.event()
        print("finish,-------", [wheel.next_process.__name__ for wheel in wheels], self.env.now)
        # self.rewrite.succeed()
        # self.rewrite = self.env.event()

    def setup(self):
        while self.pc < 10:
            self.env.process(self.run_op(self.pc))
            yield self.env.timeout(1)
            print("=="*30, self.env.now, self.pc, "\n")
            # self.rewrite.succeed()
            # self.rewrite = self.env.event()
            self.pc += 1
            self.cycle += 1

        # while self.pre_four_wheel:
        #     self.env.process(self.run_op(None))
        #     yield self.env.timeout(1)
        #     print("==" * 30, self.env.now, self.pc, "\n")
        #     self.cycle += 1

        yield self.env.timeout(10)
        print("all count", self.count)
        # yield self.write_back_reactivate

    def run(self):
        self.prepare()
        self.env.process(self.setup())
        self.env.run()


class EmuWheel:
    PROCESS = ['fetch', 'decode', 'execute', 'write_back']

    def __init__(self, env, pc, cycle, mach):
        self.mach = mach
        self.pc = pc
        self.env = env
        self.cycle = cycle
        self.next_process = self.fetch()

    @property
    def run_sort(self):
        return random.shuffle(['fetch', 'decode', 'execute', 'write_back'])

    def fetch(self):
        print("fetch pc, {}, {}".format(self.pc, self.env.now))
        self.next_process = self.decode()
        # yield self.mach.rewrite
        # print("====")
        yield self.env.timeout(1)
        # print("finish, fetch,", self.cycle, self.env.now, self.next_process.__name__)
        # yield self.fetch_reactivate

    def decode(self):
        print("decode, {}, {}".format(self.pc, self.env.now))
        self.next_process = self.execute()
        # if self.cycle < 2:
        #     yield self.env.timeout(0)
        # else:
        #     yield self.mach.rewrite & self.env.timeout(0)
        yield self.env.timeout(1)
        # print("finish, decode,", self.cycle, self.env.now, self.next_process.__name__)
        # yield self.mach.rewrite | self.env.timeout(1)
        # print(self.mach.tmp, "====")
        # yield self.env.timeout(1)
        # yield self.decode_reactivate

    def execute(self):
        print("execute, {}, {}".format(self.pc, self.env.now))
        self.next_process = self.write_back()
        yield self.env.timeout(1)
        # print("finish, execute,", self.cycle, self.env.now, self.next_process.__name__)
        # yield self.execute_reactivate

    def write_back(self):
        m = random.randint(0, 100)
        print("write_back, {}， {}, random {}".format(self.pc, self.env.now, m))
        self.mach.tmp.append(m)
        yield self.env.timeout(1)
        # print("finish, write back,", self.cycle, self.env.now, self.next_process.__name__)


if __name__ == '__main__':
    emulator = Emulator()
    emulator.run()
