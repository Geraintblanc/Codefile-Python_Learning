# ⛰️ 7.3.2 删除为特定值的所有列表元素
"""
在第三章中🀄️，我们用了函数remove()去删除列表中的特定的值。之前的可行性的原因是
是因为，要删除的值只在列表中出现一次。
如果要删除列表中所有特定值的元素，可以不断运行一个while循环，知道列表中不在包含那个
特定值 🎦
"""
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
