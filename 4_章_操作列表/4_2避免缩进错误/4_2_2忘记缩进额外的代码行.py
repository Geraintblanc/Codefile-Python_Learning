# 😀 4.2.2 忘记缩进额外的代码行
'''
循环能够运行且不会报告错误❌，但是结果可能出人意料。试图
在循环中执行多项任务，却忘记缩进其中的一些代码行时，就会出现
这种情况
'''
magicians = ['alice', 'david', 'carolian']
for magician in magicians:
    print(f"{magician.title()} that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

# ❗：
# 如果是忘记缩进额外的代码行呢
numbers = [1,3,4,5,6,6]
for num in numbers:
    print(f"This is {num}")
    print(f"The {num} is a number~.\n")
print('---------以下是忘记末尾行缩进的情况-----------------------')
numbers = [1,3,4,5,6,6]
for num in numbers:
    print(f"This is {num}")
print(f"The {num} is a number~.\n")