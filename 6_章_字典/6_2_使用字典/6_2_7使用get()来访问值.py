# ⭐ 6.2.7 使用get()来访问值
"""
使用放在括号内的键从字典中获取感兴趣的值时，可能会引发问题：
    如果指定的键不存在就会出错
"""
alien_0 = {'color': 'green', 'speed': 'slow'}
# print(alien_0['points'])
# 如果用上述的代码则会出现下列的问题
"""
Traceback (most recent call last):
  File "D:\Codefile\6_章_字典\6_2_使用字典\6_2_7使用get()来访问值.py", line 7, in <module>
    print(alien_0['points'])
          ~~~~~~~^^^^^^^^^^
KeyError: 'points'
"""
print('---------------------------------------------')
"""
第十章：
    将详细介绍如何处理类似的错误，但是就字典而言，可以使用get()方法在指定的键
    不存在时返回一个默认值，从而避免这样的错误。
"""
alien_0 = {'color': 'green', 'speed': 'slow'}

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

