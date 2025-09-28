# 🌈 在循环中♻️使用continue

"""
要返回循环开头，并根据条件测试的结果决定是否继续执行循环，可以使用continue语句，
它不像break那样不再执行余下的代码并退出整个循环；
"""

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)