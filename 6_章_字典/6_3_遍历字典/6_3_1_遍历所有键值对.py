# ⭐ 6.3 遍历字典
"""
一个python字典可能只包含几个键值对，也可能包含数百个键值对。
鉴于字典可能包含大量数据，python支持对字典进行遍历。字典可以
用于以各种方式存储信息，因此有多种遍历方式：可遍历字典的所有键值对，
也可仅遍历键或值。
"""
# 🐂 6.3.1 遍历所有的键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}
for key, value in user_0.items(): #1
    print(f"\nKey: {key}")
    print(f"Value: {value}")
"""
❗：
    如#1所示，要编写遍历字典的for循环，可声明两个变量，用于存储键和值。
    这两个变量可以使用任意名称
    for语句的第二部分包含字典名和方法items()，它返回一个键值对列表。接下来
    for循环依次将每个键值对赋给指定的两个变量。
    在上述例子中，使用这两个变量打印每个键机器相关联的值
"""
print('----例子2-------------------')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

