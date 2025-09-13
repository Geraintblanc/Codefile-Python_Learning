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
del motorcycles[0]
print(motorcycles)
'''
使用del可删除任意位置处的列表元素，条件时知道其索引
'''
## ❗: 使用方法pop()删除元素
'''
有时候，你要将元素从列表中删除，并接着使用它的值
方法pop()删除列表末尾的元素，并让你能够接着使用它；
术语pop()源自这样的类比：
        列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素
'''
motocycles_1 = ['h1','h2','h3']
print(motocycles_1)

popped_motocycle_1 = motocycles_1.pop()
print(motorcycles)
print(popped_motocycle_1) # pop()删除列表末尾的元素 此刻输出的是 h3

# ❗： 03 弹出⏏列表中任何位置处的元素
character = ['c1', 'c2', 'c3']
print(character.pop(0)) # 此时输出c1
print(character.pop())# 此时输出c3
character.insert(0,'c1') # 在列表中插入元素
character.insert(2,'c3')
first_character = character.pop(0)
print(f'The first character I written is {first_character.title()}!')

# ❗： 04： 根据值删除元素
'''
有时候，你不知道要从列表中删除的值所处的位置。如果只知道要删除的元素的值
，可以使用方法remove()
'''