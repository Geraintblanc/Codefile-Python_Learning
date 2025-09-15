# ⭐ 6.2.5 删除键值对
"""
对于字典不再需要的信息，可以使用del语句将相应的键值对彻底删除。
使用del语句时，必须指定字典名和要删除的键。
"""
# 例子：下面的代码从字典从alien_0中删除键‘points’及其值
alien_0 = {'color': 'green', 'points': 5}
print(alien_0) # {'color': 'green', 'points': 5}

del alien_0['points']
print(alien_0) # {'color': 'green'}