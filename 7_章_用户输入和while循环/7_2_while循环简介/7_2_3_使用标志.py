# ⭐ 7.2.3 使用标志
"""
在上一节的例子中，我们让程序在满足指定条件时执行特定的任务。
但在更复杂的程序中，很多不同的时间会导致程序停止运行。
在要求很多条件都满足才能运行的程序中，可以定义一个变量，用于
判断整个程序是否处于活动状态。
    ❗：标志（flag）
    这个变量称为标志flag，充当程序的交通信号灯。可以让程序在
    标志为True时继续运行，并在任何事件导致标志的值为False时
    让程序停止运行。
    这样，在while语句中就只需要检查一个条件：
    标志的当前值是否为True。然后将所有其他测试都放在其他地方，
    从而让程序更简洁。
"""
# 😅 例子：我们将在前一节的列子中添加一个标志，将其名为active，用于判断程序是否应该继续运行
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
