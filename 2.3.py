import os
from collections import namedtuple

# 2.3 元组不仅仅是不可变的列表
# 2.3.1 元组和记录
lax_coordinates = (33.9425, -118.408056)  # 洛杉矶国际机场的经纬度
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)  # 东京市的一些信息：市名、年份、人口（单位：百万）、人口变化（单位：百分比）和面积（单位：平方千米）
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]  # 一个元组列表，元组的形式为 (country_code, passport_number)
for passport in sorted(traveler_ids):  # 在迭代的过程中，passport 变量被绑定到每个元组上
    print('%s/%s' % passport)  # % 格式运算符能被匹配到对应的元组元素上

for country, _ in traveler_ids:  # for 循环可以分别提取元组里的元素，也叫作拆包（unpacking）。因为元组中第二个元素对我们没有什么用，所以它赋值给“_”占位符
    print(country)

# 2.3.2 元组拆包
latitude, longitude = lax_coordinates  # 元组拆包
print(latitude)
print(longitude)

print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print((quotient, remainder))

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

a, b, *rest = range(5)
print((a, b, rest))

a, b, *rest = range(3)
print((a, b, rest))

a, b, *rest = range(2)
print((a, b, rest))

a, *body, c, d = range(5)
print((a, body, c, d))

*head, b, c, d = range(5)
print((head, b, c, d))

# 2.3.3 嵌套元组拆包
metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),  # 每个元组内有 4 个元素，其中最后一个元素是一对坐标
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # 我们把输入元组的最后一个元素拆包到由变量构成的元组里，这样就获取了坐标
    if longitude <= 0:  # if longitude <= 0: 这个条件判断把输出限制在西半球的城市
        print(fmt.format(name, latitude, longitude))

# 2.3.4 具名元组
City = namedtuple('City', 'name country population coordinates')  # 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字。后者可以是由数个字符串组成的可迭代对象，或者是由空格分隔开的字段名组成的字符串
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))  # 存放在对应字段里的数据要以一串参数的形式传入到构造函数中（注意，元组的构造函数却只接受单一的可迭代对象）
print(tokyo)
print(tokyo.population)  # 你可以通过字段名或者位置来获取一个字段的信息
print(tokyo.coordinates)
print(tokyo[1])

print(City._fields)  # _fields 属性是一个包含这个类所有字段名称的元组
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
delhi = City._make(delhi_data)  # 用 _make() 通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟 City(*delhi_data) 是一样的
print(delhi._asdict())  # _asdict() 把具名元组以 collections.OrderedDict 的形式返回，我们可以利用它来把元组里的信息友好地呈现出来
for key, value in delhi._asdict().items():
    print(key + ':', value)
