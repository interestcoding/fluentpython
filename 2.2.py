import array
import timeit

# 2.2 列表推导和生成器表达式
# 2.2.1 列表推导和可读性
# 示例 2-1 把一个字符串变成 Unicode 码位的列表
symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    codes.append(ord(symbol))
print(codes)

# 示例 2-2 把字符串变成 Unicode 码位的另外一种写法
codes = [ord(symbol) for symbol in symbols]
print(codes)

x = 'ABC'
dummy = [ord(x) for x in x]
print(x)  # x 的值被保留了

print(dummy)  # 列表推导也创建了正确的列表

# 2.2.2 列表推导同filter和map的比较
# 示例 2-3 用列表推导和 map/filter 组合来创建同样的表单
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)

# from example code start
TIMES = 10000

SETUP = """
symbols = '$¢£¥€¤'
def non_ascii(c):
    return c > 127
"""


def clock(label, cmd):
    res = timeit.repeat(cmd, setup=SETUP, number=TIMES)
    print(label, *('{:.3f}'.format(x) for x in res))


clock('listcomp        :', '[ord(s) for s in symbols if ord(s) > 127]')
clock('listcomp + func :', '[ord(s) for s in symbols if non_ascii(ord(s))]')
clock('filter + lambda :', 'list(filter(lambda c: c > 127, map(ord, symbols)))')
clock('filter + func   :', 'list(filter(non_ascii, map(ord, symbols)))')
# from example code end

# 2.2.3 笛卡儿积
# 示例 2-4 使用列表推导计算笛卡儿积
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]  # 这里得到的结果是先以颜色排列，再以尺码排列
print(tshirts)
for color in colors:  # 注意，这里两个循环的嵌套关系和上面列表推导中 for 从句的先后顺序一样
    for size in sizes:
        print((color, size))
tshirts = [(color, size) for size in sizes  # 如果想依照先尺码后颜色的顺序来排列，只需要调整从句的顺序。我在这里插入了一个换行符，这样顺序安排就更明显了
           for color in colors]
print(tshirts)

# 2.2.4 生成器表达式
# 示例 2-5 用生成器表达式初始化元组和数组
print(tuple(ord(symbol) for symbol in symbols))  # 如果生成器表达式是一个函数调用过程中的唯一参数，那么不需要额外再用括号把它围起来
# array 的构造方法需要两个参数，因此括号是必需的。array 构造方法的第一个参数指定了数组中数字的存储方式。2.9.1 节中有更多关于数组的详细讨论
print(array.array('I', (ord(symbol) for symbol in symbols)))

# 示例 2-6 使用生成器表达式计算笛卡儿积
for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):  # 生成器表达式逐个产出元素，从来不会一次性产出一个含有 6 个 T 恤样式的列表
    print(tshirt)
