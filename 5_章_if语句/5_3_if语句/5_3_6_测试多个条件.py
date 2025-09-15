# ⭐ 5.3.6 测试多个条件
"""
if-elif-else 结构和 简单if语句的区别
    if-elif-else:结构功能强大，但是，仅适合用于只有一个条件满足的情况
        ：遇到通过了的测试后，Python就会跳过余下的测试。这种行为很好，效率很高
        让我们能够测试一个特定的条件
    简单if 语句： 有时候必须检查你关心的所有条件。
        在这种条件下，应使用一系列不包含elif和else代码块的简单if语句。
        在可能有多个条件为True且需要在每个条件为True时都采取相应措施，适合这种方法
"""
print('----------简单if语句-----------')
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza！ ")
# 简单if语句：不管前一个测试是否通过，都将进行这个测试

print('------如果使用if-elif-else结构呢---------')
# 这种结构是：有一个测试通过后，就会跳过余下的测试
requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza！ ")

"""
总之，如果只想执行一个代码块，就使用if-elif-else结构;如果要执行
多个代码块，就使用一系列独立的if语句
"""
