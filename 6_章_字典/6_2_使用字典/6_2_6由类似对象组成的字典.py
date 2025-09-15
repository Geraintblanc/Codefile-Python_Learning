# ⭐ 6.2.6 由类似对象组成的字典
"""
在我们之前的案例中，字典存储的时一个对象（游戏中的一个外星人）的多种信息，但你也可以
使用字典来存储众多对象的同一种信息。
        ❗：
        例如：假设你要调查很多人，询问他们最喜欢的编程语言，可以使用一个字典来存储
            这种简单调查的 结果：
"""
favorite_languages = {
    'jen' : 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
"""
定义好字典后，在最后一个键值对的下一行添加一个右花括号，并缩进四个空格，
使其与字典中的键对其。
一种不错的做法是，在最后一个键值对后面也加上都好，为以后在下一行添加键值对
做好准备。
"""
# 给定被调查者的名字，可以使用这个字典轻松获悉他喜欢的语言
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}")
# favorite_languages['sarah']--为获悉Sarah喜欢的语言，我们应该用左侧的代码