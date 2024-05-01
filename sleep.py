import random
import time

# 生成一个 0 到 3600 秒（即 1 小时）之间的随机数
delay_seconds = random.randint(10, 1800)

print("等待", delay_seconds, "秒...")
time.sleep(delay_seconds)
print("延迟结束")
