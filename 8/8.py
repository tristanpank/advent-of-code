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

total_scores = []
for i in range(col_len):
    for j in range(row_len):
        if i == 0 or j == 0 or i == col_len - 1 or j == row_len - 1:
            continue
        
        distance_score = 1
        distances = []
        col = [row[j] for row in trees]
        row = trees[i]
        curr_tree = trees[i][j]

        # check up
        dist = 0
        for k in range(i-1, -1, -1):
            if col[k] >= curr_tree:
                dist += 1
                break
            else:
                dist += 1
        distance_score *= dist
        distances.append(dist)

        # check down
        dist = 0
        for k in range(i+1, col_len):
            if col[k] >= curr_tree:
                dist += 1
                break
            else:
                dist += 1
        distance_score *= dist
        distances.append(dist)

        # check left
        dist = 0
        for k in range(j-1, -1, -1):
            if row[k] >= curr_tree:
                dist += 1
                break
            else:
                dist += 1
        distance_score *= dist
        distances.append(dist)

        # check right
        dist = 0
        for k in range(j+1, row_len):
            if row[k] >= curr_tree:
                dist += 1
                break
            else:
                dist += 1
        distance_score *= dist
        distances.append(dist)

        if distance_score == 374400:
            print((i, j, distance_score, distances))
        # print((i, j, distance_score, distances))
        total_scores.append(distance_score)

total_scores.sort()
print(max(total_scores))
