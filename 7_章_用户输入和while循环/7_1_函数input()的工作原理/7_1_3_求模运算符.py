# ⭐ 7.1.3 求模运算符
"""
处理数值信息时，求模运算符(%)是个很有用的工具，它将两个数相除
并返回余数：
    如果一个数可悲另一个数整除，余数就为0，因此求模运算将返回
    0。可利用这一点来判断一个数时奇数还是偶数
"""
number = input("Enter a number, and I'll tell you if it's even or odd:")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")