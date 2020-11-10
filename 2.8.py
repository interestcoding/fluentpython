import bisect
import sys

# 2.8 用bisect来管理已排序的序列
HAYSTACK = [1, 4, 5, 6, 8, 12, 15, 20, 21, 23, 23, 26, 29, 30]
NEEDLES = [0, 1, 2, 5, 8, 10, 22, 23, 29, 30, 31]

ROW_FMT = '{0:2d} @ {1:2d}    {2}{0:<2d}'


def demo(bisect_fn):
    for needle in reversed(NEEDLES):
        position = bisect_fn(HAYSTACK, needle)  # 用特定的 bisect 函数来计算元素应该出现的位置。
        offset = position * '  |'  # 利用该位置来算出需要几个分隔符号。
        print(ROW_FMT.format(needle, position, offset))  # 把元素和其应该出现的位置打印出来。


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


if __name__ == '__main__':
    # 2.8.1 用bisect来搜索
    # 示例 2-17 在有序序列中用 bisect 查找某个元素的插入位置
    # if sys.argv[-1] == 'left':  # 根据命令上最后一个参数来选用 bisect 函数。
    #     bisect_fn = bisect.bisect_left
    # else:
    #     bisect_fn = bisect.bisect
    print('DEMO:', bisect.bisect.__name__)  # 把选定的函数在抬头打印出来。
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect.bisect)
    # 以bisect_left来运行
    print('DEMO:', bisect.bisect_left.__name__)
    print('haystack ->', ' '.join('%2d' % n for n in HAYSTACK))
    demo(bisect.bisect_left)

    # 示例 2-18 根据一个分数，找到它所对应的成绩
    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])

    # 2.8.2 用bisect.insort插入新元素
