from math import hypot


class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    # 1.2.4 自定义的布尔值
    def __bool__(self):
        # return bool(abs(self))
        return bool(self.x or self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    # 1.2 如何使用特殊方法
    # 1.2.1 模拟数值类型
    # 示例 1-2 一个简单的二维向量类
    print('-' * 80)
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)
    print(v1 + v2)

    print('-' * 80)
    v = Vector(3, 4)
    print(abs(v))

    print('-' * 80)
    print(v * 3)
    print(abs(v * 3))
