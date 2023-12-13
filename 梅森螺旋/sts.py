'''
Author: Little Weak_Duck
Date: 2023-12-01 16:11:09
LastEditors: Little Weak_Duck
LastEditTime: 2023-12-12 06:48:48
FilePath: /sts.py
Description: generate sts test file
'''

from prng import MersenneTwister as random

def generate_binary_data(prng, num_bits, num_sequences):
    """生成指定数量比特的二进制数据，分割成多个序列"""
    data = bytearray()
    bits_per_sequence = num_bits // num_sequences
    for _ in range(num_sequences):
        for _ in range(bits_per_sequence // 8):
            byte = 0
            for _ in range(8):
                byte = (byte << 1) | prng.extract_number() % 2
            data.append(byte)
    return data


seed = 1234
mt = random(seed)
# 生成二进制数据（例如 8MB 的数据，分割成 8 个序列）
num_sequences = 8
binary_data = generate_binary_data(mt, 8 * 8 * 1024 * 1024, num_sequences)


# 将数据写入文件
with open('random_data.bin', 'wb') as file:
    file.write(binary_data)
