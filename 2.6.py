import dis
import traceback

# 2.6 序列的增量赋值
l = [1, 2, 3]
print(id(l))  # 刚开始时列表的 ID。
l *= 2
print(l)
print(id(l))  # 运用增量乘法后，列表的 ID 没变，新元素追加到列表上。
t = (1, 2, 3)
print(id(t))  # 元组最开始的 ID。
t *= 2
print(id(t))  # 运用增量乘法后，新的元组被创建。

# 示例 2-15 一个谜题，没人料到的结果：t[2] 被改动了，但是也有异常抛出
t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
except TypeError:
    traceback.print_exc()
print(t)

# 示例 2-16 s[a] = b 背后的字节码
# step 7: 将 s[a] 的值存入 TOS（Top Of Stack，栈的顶端）。
# step 11: 计算 TOS += b。这一步能够完成，是因为 TOS 指向的是一个可变对象（也就是示例 2-15 里的列表）。
# step 13: s[a] = TOS 赋值。这一步失败，是因为 s 是不可变的元组（示例 2-15 中的元组 t）。
print(dis.dis('s[a] += b'))
