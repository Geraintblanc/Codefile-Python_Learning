# 😀 4.1.3 在for循环结束后执行一些操作
"""
for循环结束后，通常，你需要提供总结性输出或者接着执行程序必须完成其他任务
在for循环后面，没有缩进的代码都只执行一次，不会重复执行。
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")
# 使用for循环处理数据是一种对数据集执行执行整体操作的不同方式