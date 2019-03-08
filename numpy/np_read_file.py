import numpy as np

# 读取csv文件
arr = np.loadtxt("resource/test.csv", comments=",", dtype=int)

print(arr)
