with open('input.txt') as f:
    trees = [line.strip() for line in f.readlines()]

visible = set()

row_len = len(trees[0])
col_len = len(trees)
# for i in range(col_len):
#     # check left
#     for j in range(row_len):
#         if i == 0 or j == 0 or i == col_len - 1 or j == row_len - 1:
#             visible.add((i, j))

#         elif trees[i][j] > max(trees[i][:j]):
#             visible.add((i, j))
#     for j in range(row_len):
#         if i == 0 or j == 0 or i == col_len - 1 or j == row_len - 1:
#             visible.add((i, j))

#         elif trees[i][j] > max(trees[i][j+1:]):
#             visible.add((i, j))

# for i in range(row_len):
#     col = [row[i] for row in trees]
#     for j in range(1, col_len):
#         if col[j] > max(col[:j]):
#             visible.add((j, i))
#     for j in range(col_len - 1):
#         if col[j] > max(col[j+1:]):
#             visible.add((j, i))



print(visible)
print(len(visible))