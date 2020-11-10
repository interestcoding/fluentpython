# 2.7 list.sort方法和内置函数sorted
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))  # 新建了一个按照字母排序的字符串列表。
print(fruits)  # 原列表并没有变化。
print(sorted(fruits, reverse=True))  # 按照字母降序排序。
print(sorted(fruits, key=len))  # 新建一个按照长度排序的字符串列表。因为这个排序算法是稳定的，grape 和 apple 的长度都是 5，它们的相对位置跟在原来的列表里是一样的。
# 按照长度降序排序的结果。结果并不是上面那个结果的完全翻转，因为用到的排序算法是稳定的，也就是说在长度一样时，grape 和 apple 的相对位置不会改变。
print(sorted(fruits, key=len, reverse=True))
print(fruits)  # 直到这一步，原列表 fruits 都没有任何变化。
print(fruits.sort())  # 对原列表就地排序，返回值 None 会被控制台忽略。
print(fruits)  # 此时 fruits 本身被排序。
