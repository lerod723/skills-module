import random

def play():
    user = input("Input 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    print(f'Computer chose: {computer}')

    if user == computer:
        return 'It\'s a tie!'
    
    if iswin(user, computer):
        return 'You won!'
    
    return 'You lost!'  # No need to check iswin == False here, since it's implied

def iswin(player, opponent):
    # Returns True if the player beats the opponent
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True

# Call play and print its result
print(play())