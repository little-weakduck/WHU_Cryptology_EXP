'''
Author: Little Weak_Duck
Date: 2023-12-01 15:37:28
LastEditors: Little Weak_Duck
LastEditTime: 2023-12-01 16:16:56
FilePath: /prng.py
Description: generate prng 
'''
import time

class MersenneTwister:
    def __init__(self, seed=None):
        # 如果没有提供seed则使用当前时间戳
        if seed is None or not isinstance(seed, int):
            seed = int(time.time())
        self.w, self.n, self.m, self.r = 32, 624, 397, 31
        self.a = 0x9908B0DF
        self.u, self.d = 11, 0xFFFFFFFF
        self.s, self.b = 7, 0x9D2C5680
        self.t, self.c = 15, 0xEFC60000
        self.l = 18
        self.f = 1812433253

        self.MT = [0] * self.n
        self.index = self.n + 1
        self.lower_mask = (1 << self.r) - 1
        self.upper_mask = self.lower_mask ^ self.d

        self.MT[0] = seed
        for i in range(1, self.n):
            self.MT[i] = self.int32(
                (self.f * (self.MT[i - 1] ^ (self.MT[i - 1] >> (self.w - 2))) + i))

    def int32(self, x):
        return x & 0xFFFFFFFF

    def extract_number(self):
        if self.index >= self.n:
            self.twist()

        y = self.MT[self.index]
        y ^= (y >> self.u) & self.d
        y ^= (y << self.s) & self.b
        y ^= (y << self.t) & self.c
        y ^= y >> self.l

        self.index += 1
        return self.int32(y)

    def twist(self):
        for i in range(self.n):
            x = (self.MT[i] & self.upper_mask) + \
                (self.MT[(i + 1) % self.n] & self.lower_mask)
            xA = x >> 1
            if x % 2 != 0:
                xA ^= self.a
            self.MT[i] = self.MT[(i + self.m) % self.n] ^ xA
        self.index = 0


# # 使用梅森旋转生成随机数
# seed = 5489  # 可以使用任何种子
# mt = MersenneTwister(seed)
# for _ in range(5):
#     print(mt.extract_number())
