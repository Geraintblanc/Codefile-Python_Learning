# 🍺 8.3 返回值
"""
函数并非总是直接显示输出，它还可以处理一些数据，
并返回一个或者是一组值。
函数返回的值称为返回值。
在函数中，可以使用return语句将值返回到调用函数
的代码行。
‼️ 优点：
        返回值🔙让我们能够将程序的大部分繁重工作
        移动到函数中去完成，从而简化程序。
"""

# 🌊 8.3.1 返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', ' hendrix')
print(musician)

"""
函数get_formatted_name() 的定义通过形参接受名和姓。 它将姓名合二为一，在中间
加上一个空格，并将结果赋给变量full_name.
然后将full_name 的值转换为首字母大写格式，并将结果返回到函数调用行
"""
