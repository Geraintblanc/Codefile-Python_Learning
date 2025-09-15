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
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

