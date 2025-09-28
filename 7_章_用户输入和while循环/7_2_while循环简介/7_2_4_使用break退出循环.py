# 🐮 7.2.4 使用break退出循环 ♻️
"""
要立即退出⏏️while循环，不再运行循环中余下的代码，也不管条件测试的结果如何
可以使用break语句。
break语句用于控制程序流程，可用来控制哪些代码执行，哪些代码不执行，从而让
程序按照你的要求执行你需要的代码
"""

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished."

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print(f"I'd love to go the {city.title()}!")
# 以while true打头的循环♻️将不断运行，直到遇到break语句，
# 用户输入‘quit’后，将执行break语句，导致python退出循环

"""
⚠️：
    在任何Python循环中都可以break语句。
"""