import random as rn

bots_choice = ['Snake', 'Water', 'Gun']
comp = rn.randint(0, 2)
bot = bots_choice[comp]

players_choice = ['Snake', 'Water', 'Gun']
user = int(input('Enter your move:\n0 for Snake\n1 for Water\n2 for Gun\n'))
player = players_choice[user]


def game(player, bot):
    if player == bot:
        return 0
    elif player == players_choice[2] and bot == bots_choice[1]:
        return -1
    elif player == players_choice[0] and bot == bots_choice[2]:
        return -1
    elif player == players_choice[1] and bot == bots_choice[0]:
        return -1
    return 1

print('Your move:', player)
print("Bot's move:", bot)

points = game(player, bot)
if points == 0:
    print('Oops, Its a Draw!')
elif points == -1:
    print('Sad, You Lose!')
else:
    print('Yay, You won!')


