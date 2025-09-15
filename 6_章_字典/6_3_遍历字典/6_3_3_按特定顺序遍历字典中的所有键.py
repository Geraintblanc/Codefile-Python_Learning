# ⭐ 6.3.3 按特定顺序遍历字典中的所有键
"""
从python3.7 起，遍历字典时将按插入的顺序返回其中的元素。不过在有些情况下，
你可能要按照与此不同的顺序遍历字典。
要以特定顺序返回元素，一种方法时for循环中对返回的键进行i排序。为此，可以使用
函数sorted()来获得按特定顺序排列的键列表的副本：
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
"""
这条for语句类似于🐟其他for语句，不同之处是对方法dictionary.keys()的结果
调用了函数sorted()。这让Python列出字典中的所有键，并在遍历前对这个列表进行排序。
输出表示：
    按顺序显示了所有被调查者的名字：
    结果如下：
        Edward, thank you for taking the poll.
        Jen, thank you for taking the poll.
        Phil, thank you for taking the poll.
        Sarah, thank you for taking the poll.
"""