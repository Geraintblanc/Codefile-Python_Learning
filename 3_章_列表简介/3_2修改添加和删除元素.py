# 3.2 修改、添加和删除元素
'''
你创建的大多数哦 列表是动态的，这意味着列表创建后，将随着程序的运行增删元素
'''
## 😀3.2.1 修改列表元素
'''
修改列表元素的语法与访问列表元素的语法类似。要修改列表元素，可以指定列表名和要修改
的元素的索引，再指定该元素的新值
'''
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

## 😀 3.2.2 在列表中添加元素
# 你可能出于众多原因要在列表中添加新元素
# ❗： 01： 在列表末尾添加元素
'''
在列表中添加新元素时，最简单的方式时将元素添加（append）
到列表，它将添加到列表末尾。
'''
motorcycles.append('xinzeng') # 方法append()让动态地创建列表易如反掌
print(motorcycles)

# ❗： 02. 在列表中插入元素
'''
使用方法insert()，可在列表的任何位置添加新元素，为此你需要指定新元素的索引和值
'''
motorcycles.insert(0,'insertxinzeng')
print(motorcycles)

## 😀 3.2.3 从列表中删除元素
# 你经常需要从列表中删除一个或者多个元素
## ❗：01.使用del语句删除元素
'''
如果知道要删除的元素在列表中的位置，可使用del语句
'''
