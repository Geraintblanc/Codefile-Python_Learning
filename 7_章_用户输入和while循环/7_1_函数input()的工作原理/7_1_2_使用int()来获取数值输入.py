# ⭐ 7.1.2 使用int()来获取数值输入
"""
使用函数input()时，python将用户输入解读为字符串
"""
age = input("How old are you?")
print(f"I am {age}!")

print('------------------------------')
height = input("How tall are you, in inches?")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
"""
逐行解释（简明）

height = input("How tall are you, in inches?")
input() 会在终端显示提示并等待用户输入，返回值是一个
字符串（str）。无论你输入 65、65、65.0、sixty five，input()
 都把它当作字符串返回并赋值给变量 height。

height = int(height)
这是关键：int(...) 是 Python 的内建函数，用来把
一个可被理解为整数的值变成整数类型（int）。这里把字符
串转换成整数后再赋回 height 变量。转换失败会抛出 
ValueError（程序会中断，除非你捕获这个异常）。

if height >= 48:
因为上一步 height 已经是整数，所以可以做数值比较（>=）。
如果高度不小于 48 英寸就进入第一个分支，否则进入 else。

print("\nYou're tall enough to ride!") 
/ print("\nYou'll be able to ride when you're a little older.")
\n 是换行字符，打印时会先空一行再输出文本。
"""