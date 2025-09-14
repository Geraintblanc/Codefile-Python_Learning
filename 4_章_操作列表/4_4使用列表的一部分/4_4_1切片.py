# 🐂： 4.4 使用列表的一部分
'''
在第三章中，我们进行了单个列表元素的访问。
    此时，我们在第四章，一直在学习如何处理列表的所有元素。
    你还可以处理列表的部分元素，Python称之为切片。
'''
# ♥ 4.4.1 切片
'''
要创建切片，可以指定要使用的第一个元素和最后一个元素的指引。
与函数range()一样，python在到达第二个索引之前的元素后停止。
'''
运动员 = ['xiaobai','xiaohuang','xiaohei','xiaosan','xiaosi','xiaowu']
print(运动员[0:3]) #['xiaobai', 'xiaohuang', 'xiaohei']
# 要输出列表中的三个元素，需要指定索引0和3，这将返回索引为0，1，2的元素
print(运动员[1:4]) # ['xiaohuang', 'xiaohei', 'xiaosan']

# 若是没有指定第一个索引，python将自动从列表开头开始
print(运动员[:3]) #['xiaobai', 'xiaohuang', 'xiaohei']

# 类似的
print(运动员[2:]) #['xiaohei', 'xiaosan', 'xiaosi', 'xiaowu']
# 无论列表多长，这种语法都能够让你输出从特定位置到列表末尾的所有元素
print(运动员[-4:]) # ['xiaohei', 'xiaosan', 'xiaosi', 'xiaowu']
