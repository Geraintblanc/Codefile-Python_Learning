# ♥ 4.5 元组
"""
列表非常适合用于存储在程序运行期间可能变化的数据。
    列表是可以修改的，这对于处理网站的用户列表或者游戏中的角色列表至关重要。
    然而，有时候需要创建一系列不可修改的元素。
    Python将不能修改的值成为不可变的，而不可变的列表称之为元组。
"""
# 🐂 4.5.1 定义元组
'''
元组看起来很像列表，但使用圆括号而非中括号来标识。
定义元组后，就可以使用索引来 访问其元素，就像访问列表元素一样。
'''
# 例子：
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# ✳ 如果我们尝试修改元组dimensions的一个元素
# dimensions[0] = 250
# print(dimensions[0])
"""
Traceback (most recent call last):
  File "D:\Codefile\4_章_操作列表\4_5元组\4_5_1定义元组.py", line 19, in <module>
    dimensions[0] = 250
    ~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""
#以上就是修改后报错的，我把修改的代码给重新修改了

"""
❗：
    注意：attention：
        严格的来说，元组都是有逗号标识的，圆括号只是让元组看起来更整洁、更清晰。
        如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号：
            my_t = (3, )
        创建只包含一个元素的元组通常没有意义，但自动生成的怨怒有可能只有一个元素。
"""