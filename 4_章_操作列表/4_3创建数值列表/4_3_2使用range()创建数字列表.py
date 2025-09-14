# 😀 4.3.2 使用range（）创建数字列表

'''
要创建数字列表，可以使用函数list()将range()的结果
直接转换为列表。
如果将range()，作为list()的参数，输出将是一个数字列表。
'''
numbers = list(range(1,6))
print(numbers)
# 上面输出的结果时：[1, 2, 3, 4, 5]

### ❗：使用range（）时，还可以指定步长。为此可以给这个函数指定第三个参数，python
### ❗： python可以根据这个步长来生成数
# 练习： 代码打印1~10的偶数
偶数 = list(range(2,11,2))
print(偶数) # [2, 4, 6, 8, 10]

'''
使用函数range()几乎可以创建任何需要的数集
'''
## 下面的代码演示了如何将前10个整数的平方加入一个列表中：
## Squares.py 此刻 square是临时变量
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print('----为了让代码更简洁，可以不使用临时变量square-----')
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)
"""
❗：
    创建更复杂的列表时，可以使用上述的两种的方法任意一种；
    有时候，使用临时变量会让代码更易读；
    而在其他情况下，这样做会让代码无所谓的变长。
    但是我们首先需要考虑的是：
    编写清晰易懂且能完成所需功能的代码，等到审核代码时，再考虑
    采用更加高效的方法。
"""