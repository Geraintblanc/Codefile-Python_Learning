# ⭐6.3.4 遍历字典中的所有值
"""
如果主要对字典包含的值感兴趣，可使用方法values()
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
"""
❗：
    这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，
    但是如果被调查者很多，最终的列表可能包含大量的重复项。为了剔除重复项，可使用集合
    ❗set,集合中的每个元素都必须时独一无二的
"""
print('----------set集合减去重复------------')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())