###字符串
# 字符串就是一系列字符，在python中，用引号括起的都是字符串，
# 其中的引号可以是单引号也可以是双引号
# 2.3.1 使用方法修改字符串的大小写
### 1 改变首字母大小写
name = 'ada lovelace'
print(name.title())
# Ada Lovelace

### 2 全部变成大写
print(name.upper())
# ADA LOVELACE
### 3. 全部变成小写
print(name.lower())
#ada lovelace

# 2.3.2 在字符串中使用变量
first_name = 'zihao'
last_name = 'bai'
full_name = f'{first_name} {last_name}'
print(full_name)
"""
要在字符串中插入变量的值，可在引号前加个字母f,再将要插入的变量放
在花括号内，这样当Python显示字符串时，将把每个变量都替换成其值
这种字符串名为-------f字符串
f是format（设置格式）的简写，因为python通过把花括号内的变量替换
为其值来设置字符串的格式
f字符串是python3.6中引入的
"""

# 2.3.3 使用制表符或者换行符来添加空白
"""
\t 是制表符
\n 是换行符
"""
print('python')
#python
print('\tpython')
#   python
print('Languages:\npython\nc\njavascript')
#Languages:
#python
#c
#javascript
print('Languages:\n\tpython\n\tc\n\tjavascript')
#Languages:
#   python
#   c
#   javascript

## 2.3.4 删除空白
# .rstrip() 是删除的语法
favorite_language = 'Python    '
print(favorite_language)
print(favorite_language.rstrip())
# 剔除字符串开头的空白 .lstrip()
# 同时剔除字符串两边的空白 .strip()

#2.3.5 使用字符串时避免语法错误
"""
语法错误，是一种时不时会遇到的错误，程序中包含非法的python代码时
就会导致语法错误
"""
