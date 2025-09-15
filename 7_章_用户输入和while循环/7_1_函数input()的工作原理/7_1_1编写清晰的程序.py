# ⭐ 7.1 函数input（）的工作原理
"""
函数input()让程序暂停运行，等待用户输入一些文本。获取
用户输入后，python将其赋给一个变量，方便使用。
"""
# ☀ 几个简单的例子：
message = input("Tell me something, and I wil lrepeat it back to you:")
print(message)
"""
函数input()接受一个参数--要向用户显示的提示（prompt）或说明，让用户该知道怎么做。
"""
# 🌙 ☀ ： 7.1.1 编写清晰的程序
"""
每当使用函数input()时，都应该指定清晰易懂的提示，准确地指出希望用户提供什么样的
信息--- 指出用户应该输入何种信息的任何提示都行。
"""
print('-----------example2-----------')
name = input("Please enter your name:")
print(f"\nHello, {name}!")

"""
有时候，提示可能超过一行。例如：你可能需要指出获取特定输入的原因。
在这种情况下，可将提示赋给一个变量， 再将该变量传递给函数input().
这样，即便提示超过一行，input()语句也会非常清晰。
"""
# greeter.py
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")