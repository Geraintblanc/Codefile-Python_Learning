# 🎆 8.1.2 实参和形参
"""
变量username是一个形参数（parameter）
    🀄️ 即函数完成工作所需的信息
在代码greet_user('zihao')中，值'zihao'是一个实参（argument）
    🀄️ 即调用函数时传递给参数的信息


"""
def greet_user(username):
    print(f'Hello, {username.title()}!')

greet_user('zihao')