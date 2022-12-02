with open('input.txt') as f:
    games = f.readlines()

round_scores = {'X': 0, 'Y': 3, 'Z': 6}
move_loss = {'A': 'C', 'B': 'A', 'C': 'B'}
move_wins = {'A': 'B', 'B': 'C', 'C': 'A'}
move_scores = {'A': 1, 'B': 2, 'C': 3}
score = 0

for game in games:
    moves = game.split()
    if moves[1] == 'X':
        score += move_scores[move_loss[moves[0]]]
    elif moves[1] == 'Y':
        score += 3 + move_scores[moves[0]]
    elif moves[1] == 'Z':
        score += 6 + move_scores[move_wins[moves[0]]]



# move_scores = {'X': 1, 'Y': 2, 'Z': 3}
# move_wins = {'X': 'C', 'Y': 'A', 'Z': 'B'}
# move_draws = {'X': 'A', 'Y': 'B', 'Z': 'C'}
# score = 0

# for game in games:
#     moves = game.split()
#     score += move_scores[moves[1]]
#     if moves[0] == move_draws[moves[1]]:
#         score += 3
#     elif moves[0] == move_wins[moves[1]]:
#         score += 6

print(score)
