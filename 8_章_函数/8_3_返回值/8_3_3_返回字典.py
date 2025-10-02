# 🐳 8.3.3 返回字典

"""
函数可以返回任何类型的值，包括列表和字典等较为复杂的
数据结构。

"""
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)
"""
函数build_person() 接受🉑名和姓，并将这些值放到字典中。存储first_name
的值时，使用的键为'first', 而存储last_name 的值时，使用的键为'last'。最后
返回表示人的整个字典
"""

"""
这个函数接受简单的文本信息，并将其放在一个更合适的数据结构中，让我们不仅能打印
这些信息，还能以其他方式处理他们。
当前，字符串'jimi'和'hendrix'被标记为名和姓。
我们可以轻松的扩展这个函数，使其接受可选值，如：
中间名、年龄、职业或者其他我们要存储的信息。
"""

def build_person(first_name, last_name, age=None):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name, 'age': age}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age = 27)
print(musician)
