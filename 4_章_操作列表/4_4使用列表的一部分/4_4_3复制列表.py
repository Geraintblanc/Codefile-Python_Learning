# ♥ 我们经常要根据既有的列表创建全新的列表
'''
要复制列表，可创建一个包含整个列表的切片，方法是同时省略其实索引和终止索引
    （[:]）
    这让python创建一个始于第一个元素、种植与最后一个元素的切片，即整个列表的副本
'''
# foods.py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)
#My favorite foods are:
#['pizza', 'falafel', 'carrot cake']

print("\nMy friend's favorite foods are:")
print(friend_foods)
#My friend's favorite foods are:
#['pizza', 'falafel', 'carrot cake']

"""
为了核实确实有两个列表，如果我们在每个列表中都添加一种食品，并且核实每个列表都记录
了相对应人员喜欢的食品：
"""
print('-----------核实我们确实创建了两个表----------')
my_foods.append('caannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)