a = 3.14*3.14
print("3.14*3.14","=","%.2f"%a)
print('3.14的平方：',"%.2f"%a)
b = 100/3
print('100/4的商：',"%.3f"%b)
c = 2**5
print('2的5次方:',c)
d = 100%3
print('100除以3的余数:',d)
xing = "hong"
ming = "sheng"
print("姓名:",xing+ming)
e = ming*3
print(e)
name = "hongsheng"
age = 13.8
print("我的名字是:%s,今年%d岁" % (name,age))
print('我的名字是{}, 今年{:.2f}岁'.format(name, age))
shengao = 1.68
tizhong = 60
print('我的身高是{:.2f},体重是{}千克'.format(shengao,tizhong))
a = "123"
b = 456
num = int(a)
converted_num = str(b)
print(converted_num, type(converted_num))