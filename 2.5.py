# 2.5 对序列使用+和*
l = [1, 2, 3]
print(l * 5)
print(5 * 'abcd')

# 示例 2-12 一个包含 3 个列表的列表，嵌套的 3 个列表各自有 3 个元素来代表井字游戏的一行方块
board = [['_'] * 3 for i in range(3)]  # 建立一个包含 3 个列表的列表，被包含的 3 个列表各自有 3 个元素。打印出这个嵌套列表。
print(board)
board[1][2] = 'X'  # 把第 1 行第 2 列的元素标记为 X，再打印出这个列表。
print(board)

# 示例 2-13 含有 3 个指向同一对象的引用的列表是毫无用处的
weird_board = [['_'] * 3] * 3  # 外面的列表其实包含 3 个指向同一个列表的引用。当我们不做修改的时候，看起来都还好。
print(weird_board)
weird_board[1][2] = 'O'  # 一旦我们试图标记第 1 行第 2 列的元素，就立马暴露了列表内的 3 个引用指向同一个对象的事实。
print(weird_board)

row = ['_'] * 3
board = []
for i in range(3):
    board.append(row)  # 追加同一个行对象（row）3 次到游戏板（board）。

board = []
for i in range(3):
    row = ['_'] * 3  # 每次迭代中都新建了一个列表，作为新的一行（row）追加到游戏板（board）。
    board.append(row)
print(board)
board[2][0] = 'X'  # 正如我们所期待的，只有第 2 行的元素被修改。
print(board)
