opponent_mapping = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
response_mapping = {'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}

who_beats_who = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

points = {'rock': 1, 'paper': 2, 'scissors': 3}
outcome_points = {'loss': 0, 'draw': 3, 'win': 6}

with open('day2/data.txt', 'r') as file:
    lines = file.read().strip()

rounds = lines.split('\n')

total_points = 0

for round in rounds:
    plays = round.split(' ')

    opponent = opponent_mapping[plays[0]]
    my_response = response_mapping[plays[1]]

    am_i_winner = who_beats_who[my_response] == opponent
    is_draw = opponent == my_response

    # Running total.
    total_points += points[my_response]

    if (am_i_winner):
        total_points += outcome_points['win']
    elif (is_draw):
        total_points += outcome_points['draw']
    else:
        total_points += outcome_points['loss']

# Part 1: Real answer: 10595. Sample answer: 15.
print(f'Total points: {total_points}')
