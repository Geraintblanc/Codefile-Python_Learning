# 🌙 7.2.2 让用户选择何时退出
"""
可以使用while循环让程序在用户原意是不断运行，如下面的程序，
我们在其中定义了一个退出值，只要用户输入的不是这个值，程序就
将接着运行：
"""
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)