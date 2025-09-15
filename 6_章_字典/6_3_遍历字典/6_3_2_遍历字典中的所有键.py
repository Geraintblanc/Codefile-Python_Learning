# ⭐ 6.3.2 遍历字典中的所有的键
"""
在不需要使用字典中的值时，方法keys()很有用。
    我们下面的例子：
    遍历字典favorite_languages，并将每个被调查者的名字都打印出来。
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in favorite_languages.keys(): #去掉keys()后结果也是不变的，但是用keys()，这样可以让代码更加容易理解
    print(name.title())
