# coding=utf-8
import hashlib
import random
import psutil

data = []

# 去获取cpu的详细时间
cpu_detail = psutil.cpu_times()
data.extend(cpu_detail)
print("CPU的详细信息:{}".format(cpu_detail))


# psutil获取系统cpu使用率的方法是cpu_percent()
# 两个参数，分别是interval和percpu,
# interval指定的是计算cpu使用率的时间间隔，
# percpu则指定是选择总的使用率还是每个cpu的使用率。(默认为False)
cpu_total_percent = psutil.cpu_percent(interval=1)
print(f"当前CPU总使用率为:{cpu_total_percent}%")
data.append(cpu_total_percent)

each_cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
data.extend(each_cpu_percent)
print(f"当前每个CPU使用率为:{each_cpu_percent}")
# print(data)

# cpu详细使用率
cpu_times_percent = psutil.cpu_times_percent(interval=1, percpu=False)
print(f"当前CPU总详细使用率为:{cpu_times_percent}%")
data.extend(cpu_times_percent)

# cpu状态
cpu_stats = psutil.cpu_stats()
data.extend(cpu_stats)
print(f"cpu当前状态:{cpu_stats}")


# cpu频率
# freq = psutil.cpu_freq()
# print(f"cpu的频率:{freq}")

# 虚拟内存 总内存
virtual_memory = psutil.virtual_memory()
data.extend(virtual_memory)
print(f"虚拟内存信息:{virtual_memory}")

# 交换分区
swap_memory = psutil.swap_memory()
print(f"交换分区:{swap_memory}")
data.extend(swap_memory)

# 获取硬盘信息
# disk = psutil.disk_partitions()
# print(f"硬盘的信息:{disk}")

# 获取分区状态
disk_usage = psutil.disk_usage('/')
print(f"'/'分区状态:{disk_usage}")
data.extend(disk_usage)

# 获取单个分区的IO个数
disk_io_counters = psutil.disk_io_counters(perdisk=False)
print(f"单个分区的io个数:{disk_io_counters}")
data.extend(disk_io_counters)

print(data)
random.shuffle(data)
print(data)

data_str = "".join(str(i) for i in data)
print(data_str)
# 应用哈希函数
hash_obj = hashlib.sha256()
hash_obj.update(data_str.encode())
hash_digest = hash_obj.hexdigest()
