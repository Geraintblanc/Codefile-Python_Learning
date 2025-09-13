# 第三章
'''
列表让你能够在一个地方储存成组的信息，其中可以只包含几个元素，也可以包含数百万
个元素，列表是新手可直接使用的最强大的python功能之一
'''
# 在python中，勇敢‘[]’表示列表，并用都好分隔其中的元素
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# 😀3.1.1 访问列表元素
'''
列表是有序集合，因此要访问泪飙的任意元素，只需将该元素的位置（索引）告诉
python即可。
注意🐖：这个公式是：元素[索引]
'''
print(bicycles[0])

# 可以结合title()公式
print(bicycles[1].title())

## 😀 3.1.2 索引从0而不是1开始
'''
在python中，第一个列表元素的索引为0，而不是1.
🐖注意： 
❗：
python为访问最后一个列表元素提供了一种特殊语法，通过将索引指定为-1，可让
python返回最后一个列表元素
'''
print(bicycles[-1]) # 访问最后一个元素

