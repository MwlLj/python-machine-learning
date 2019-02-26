import numpy as np
import random

# 创建方式1
arr1 = np.array([1, 2, 3])

print(arr1)
print(type(arr1))

# 创建方式2
arr2 = np.array(range(0, 10, 2))
print(arr2)

# 创建方式3
arr3 = np.arange(0, 10, 2)
print(arr3)


# 指定数组中元素的类型
arr4 = np.array([1, 0, 1, 0], dtype=bool)
print(arr4)

# 更新数组中元素的类型
arr5 = arr4.astype("int")
print(arr5)


# roud 方法 (保留小数点位数)
arr7 = np.array([random.random() for i in range(10)])
print(arr7)
arr8 = np.round(arr7, 3)
print(arr8)
