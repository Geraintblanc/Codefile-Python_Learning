# 🗼8.3.2 让实参变成可选的
"""
有时候需要让实参变成可选的，这样使用函数的人就能只在必要时提供额外的
信息。
可使用默认值来让实参变成可选的。
"""
def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('join','lee', 'hooker')
print(musician)


print('-------------第二行代码------------------')
"""
注意⚠️：
    并非所有的人都有中间名，但是如果调用这个函数时只提供了名和姓，它将不能正确运行。为了让中间名变成可选的，
    可以形参middle_name指定一个空的默认值，并在用户没有提供中间名的时候也能使用这个形参。
    为了让get_formatted_name()在没有提供中间名的情况下依然可行，可将形参middle_name的默认值设置为空
    字符串，并将其移到形参列表的末尾。
"""

def get_formatted_name(first_name, last_name, middle_name=''):
    """"""

