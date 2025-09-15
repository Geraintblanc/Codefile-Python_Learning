# ⭐ 6.2 使用字典
"""
在python中，字典是一系列键值对。
    每个键 都与一个值相关联，你可以使用键来访问相关联的值。
    与键相关联的值可以是数、字符串、列表、乃至字典。。
    事实上，可将任何python对象用作字典中的值。
❗：
在python中，字典用放在花括号 {} 中的一系列键值对表示：
    alien_0 = {'color': 'green', 'points': 5}
    键值对 是两个相关的值。
    指定键时，python将返回与之相关联的值。
    键和值之间用冒号分离，而键值对之间用逗号分隔。
最简单的字典只有一个键值对：：
    ❗ alien_0 = {'color': 'green'}
"""
# 😀 6.2.1 访问字典中的值
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points! ")