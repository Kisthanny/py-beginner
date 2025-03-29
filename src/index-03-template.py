# 练习9
pi = 3.14
answer_1 = pi ** 2
answer_2 = 100 / 3
answer_3 = 2 ** 5
answer_4 = 100 % 3
print(f'3.14的平方: {answer_1:.2f}')
print(f'100除以3: {answer_2:.3f}')
print(f'2的5次方: {answer_3}')
print(f'100除以3的余数: {answer_4}')

# 练习10
mySurname = '琦'
myLastName = '洪'
myName = myLastName + mySurname
repeatName = myName * 3
slicedLastName = myName[0:1]
print(f'我的姓名：{myName}')
print(f'重复名字: {repeatName}')
print(f'切片姓氏：{slicedLastName}')

# 练习11
name = 'kk'
age = 8
height = 1.1
weight = 30
sportName = '高尔夫'
sportFreq = 5
print('我的名字是%s, 今年%d岁' % (name, age))
print('我的身高是{:.2f}米, 体重是{:d}千克'.format(height, weight))
print(f'我喜欢的运动是{sportName}, 每周运动{sportFreq}次')

# 练习12
my_string = '123'
my_number = 456
converted_string = int(my_string)
converted_number = str(my_number)
print(f'my_string转换前，值: {my_string}, 类型: {type(my_string)}')
print(f'my_string转换后，值: {converted_string}, 类型: {type(converted_string)}')
print(f'my_number转换前，值: {my_number}, 类型: {type(my_number)}')
print(f'my_number转换后，值: {converted_number}, 类型: {type(converted_number)}')
