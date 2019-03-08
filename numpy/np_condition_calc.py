import numpy as np

# numpy 数组的条件运算

print("原数组")
arr = np.arange(24).reshape((6, 4))
print(arr)
print("*"*100)

# 显示大于10
print("显示大于10")
print(arr>10)
print("*"*100)

# 找出大于10的位置
print("找出大于10")
print(arr[arr>10])
print("*"*100)

# 设置大于10的为100
print("将大于10的设置为100后的结果")
tmp = arr.copy()
tmp[tmp>10] = 100
print(tmp)
print("*"*100)

# 将小于10的改为100, 大于10的改为200
print("将小于10的改为100, 大于10的改为200")
tmp = np.where(arr<10, 100, 200)
print(tmp)
print("*"*100)

# 将小于10的设置为10, 大于20的设置为20
print("将小于10的设置为10, 大于20的设置为20")
tmp = np.clip(arr, 10, 20)
print(tmp)
print("*"*100)
