# 🐉 4.5.3 修改元组变量
"""
虽然不能修改元组的元素，但是可以给存储元组的变量赋值。
    比如如果修改前述dimension的尺寸，可以重新定义整个元组：
"""
dimensions = (200, 50)
print("Original dimensions:")
for dimension  in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
