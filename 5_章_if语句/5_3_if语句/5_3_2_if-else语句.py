# ⭐ 5.3.2 if-else语句
"""
我们经常需要在条件测试时执行一个操作，在没有通过时执行另一个操作。在
这种情况下，可以使用Python提供的if-else语句。
if-else语句块类似于简单的if语句，但是其中的else 语句让你能够在指定
条件测试未通过时要执行的操作。
"""
age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")
"""
Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!
"""
"""
上述的代码之所以可行，是因为只存在两种情形
if-else结果适用于让Python执行两种操作之一的情形。
"""