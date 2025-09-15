# ⭐ 6.2.2 添加键值对
"""
字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可以依次
指定字典名、用方括号括起的键和相关联的值。
"""
alien_0 = {'color':'green', 'points':5}
print(alien_0) # {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0) # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}