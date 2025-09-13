# 😀 3.3 组织列表
'''
在你创建的列表中，元素的排列顺序常常是无法预测的，因为你并非总能控制
用户提供数据的顺序。
'''
## 3.3.1 😂 使用方法sort（）对列表永久排序
'''
Python方法sort()让你能够较为轻松的对列表进行排序
sort()是对列表永久的进行排序
'''
cars = ['byd','audi','toyota','subaru','bmw']
cars.sort() # 方法sort（）永久性的修改列表元素的顺序
print(cars)
# 还可以按照与字母顺序相反的顺序排列元素，只需向
# sort()方法传递参数reverse=True即可
cars.sort(reverse=True)  # sort()方法传递参数reverse=True
print(cars)
print('----------------------------------')
## 3.3.2 🆒 使用sorted()对列表临时排序
'''
要保留列表元素原来的排列顺序，同时以特定的顺序呈现他们，可使用函数sorted()。
函数sorted()让你能够按照特定顺序显示列表元素，同时不影响他们在列表中的原始
排列顺序
'''
print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)
'''
❗：
注意：attention： 调用函数sorted（）后，列表元素的排列顺序并没有变，
如果要按与字母顺序相反的顺序显示列表，也可向函数sorted（）传递参数，
reverse=True
'''
## 😀 3.3.3 倒着打印列表
'''
要反转列表元素的排列顺序，可以使用方法reverse()
'''
num = [1,2,3,4,5,6,7,9,8]
print(num)

num.reverse() # 这里是倒着打印列表，但是并未排序
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num) # 注意reverse=True这里的True要大写
'''
🐖注意：：：：
方法reverse()永久的修改列表元素的排列顺序，但可以随时恢复到原来的排列顺序 ，
只需要对列表再次调用reverse()即可
'''
## 😀 3.3.4 确定列表的长度
'''
使用函数len()，可快速获悉列表的长度
'''
num_2 = [1,2,3,5,4,6,7,]
len(num_2)
print(len(num_2))

