# 😀 4.2.4 循环后不必要的缩进
'''
如果不小心锁进了应该在循环结束后执行的代码，这些代码将针对
每个泪飙元素重复执行。
在有些情况下，这可能导致Python报告语法错误，但是大多数情况
下，这只会导致逻辑错误。
'''
magicians =['alice', 'david', 'zihao']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick~")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

print("Thank you everyone, that was a great magic show!")

print('-------------循环后不必要的缩进，情况如下--------------------------')

magicians =['alice', 'david', 'zihao']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick~")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

    print("Thank you!") # 这种就是循环后不必要的缩进



