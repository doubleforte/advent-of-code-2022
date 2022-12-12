opponent_mapping = {'A': 'rock', 'B': 'paper', 'C': 'scissors'}
required_outcome_mapping = {'X': 'loss', 'Y': 'draw', 'Z': 'win'}

who_beats_who = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

points = {'rock': 1, 'paper': 2, 'scissors': 3}
outcome_points = {'loss': 0, 'draw': 3, 'win': 6}


def get_response(provided: str, outcome: str):
    match outcome:
        case 'draw':
            return provided

        case 'loss':
            return who_beats_who[provided]

        case 'win':
            for winner, loser in who_beats_who.items():
                if loser == provided:
                    return winner


with open('day2/data.txt', 'r') as file:
    lines = file.read().strip()

rounds = lines.split('\n')

total_points = 0

for round in rounds:
    plays = round.split(' ')

    required_outcome = required_outcome_mapping[plays[1]]

    opponent = opponent_mapping[plays[0]]
    my_response = get_response(opponent, required_outcome)

    print(f'they played: {opponent}, required outcome: {required_outcome}, mine: {my_response}')  # noqa
    print('---')

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

# Part 2: Real answer: 9541. Sample answer: 12.
print(f'Total points: {total_points}')
