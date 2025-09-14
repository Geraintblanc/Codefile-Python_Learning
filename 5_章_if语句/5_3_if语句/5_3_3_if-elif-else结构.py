# ⭐ 5.3.3 if-elif-else结构
"""
我们经常要检查超过两个的情形，为此可以使用Python提供的if-elif-else
结构。
python只执行if-elif-else结构中的一个代码块。它依次检查每个条件测试，直到
遇到通过了的条件测试。
测试通过后，python将执行紧跟在它后面的代码，并跳过余下的测试。
"""
'''
下面只需要使用if语句，如何确定门票价格：
    4岁以下免费；
    4~18随收费25美元；
    18岁（含）以上收费40美元
'''
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
"""
❗：
    elif代码其实是另一个if测试，仅在前面的测试未通过时才会运行
"""
print('-----------为了让代码简洁可以不在if-elif-else代码中打印门票价格，而只是在其中设置价格，并添加一个简单的调用---')
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")
'''
下面的这种代码，除了效率更高，这些修订后的代码还更容易修改：
    要调整输出内容的内容，只需要修改一个而不是三个函数调用print()
'''