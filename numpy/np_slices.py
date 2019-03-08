import numpy as np

# numpy array 切片
arr = np.arange(24).reshape((6, 4))
print("原数组:")
print(arr)
print("*"*100)

# 通用切片法则:
# (行, 列)
# 行/列: : -> 表示全部
# 行/列: [] -> 表示单个

# 获取第二行的全部
print("第二行")
print(arr[1,:])
print("*"*100)

# 获取第二列的全部
print("第二列")
print(arr[:,1])
print("*"*100)

# 获取第2, 3行的全部
print("第2, 3行")
print(arr[[1, 2],:])
print("*"*100)

# 获取第2, 3列的全部
print("第2, 3列")
print(arr[:,[1, 2]])
print("*"*100)

# 获取(2, 3), (4, 5)的值
print("(2, 3) (3, 3) 的值")
print(arr[[1, 2],[2, 2]])
print("*"*100)
