# ⭐ 5.3 if 语句
"""
理解条件测试后，就可以开始编写if语句了。
"""
# 😀 5.3.1 简单的if 语句
# ❗：最简单的if语句只有一个测试和一个操作：
age = 19
if age >= 18:
    print("You are old enough to vote!")
"""
在if语句中，缩进的作用与for循环中相同，如果测试通过了，
将执行if语句后面所有的缩进的代码行，否者将忽略他们。
在紧跟if语句后面的代码块中，可根据需要包含任意数量的代码行。
"""
print('-----------更新-----------')
age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
