import numpy as np

# shape 属性: 如果是一维的, 就是一维元组, 如果是二维的, 就是二维元组 ...
arr1 = np.arange(12)
print(arr1.shape)
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2.shape)

# reshape 方法 (改变数组的维度)
arr3 = arr2.reshape((3, 2))
print(arr2)
print(arr3)
arr4 = arr2.reshape((6,))
print(arr4)

# flatten 方法 (将多维数组转换为一维数组)
arr5 = arr2.flatten()
print(arr5)
