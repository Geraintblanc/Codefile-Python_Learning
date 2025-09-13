# 😀 4.2 避免缩进错误
'''
Python 根据缩进来判断代码行与前一个代码行的关系。Python通过使用缩进让代码
更容易读，简单来说，它要求你使用缩进让代码整洁而结构清晰。
'''
## 🆒 4.2.1 忘记缩进
'''
对于for语句，后面属于循环组成部分的代码行，一定要缩进，如果忘记缩进，python会提醒：
    for语句后面的代码行缩进，可以消除这种缩进错误
'''
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)