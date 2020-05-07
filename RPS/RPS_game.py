# rock paper scissors game
# simone christen
# adapted from ch 2 of 'automate the boring stuff with python' by al sweigart

import random, sys
print('ROCK, PAPER, SCISSORS!')

# these variables keep track the number of wins, losses and ties
wins = 0
losses = 0
ties = 0
while True: # the main game loop
    print('%s Wins, %s Losses, and %s Ties'%(wins, losses, ties))
    while True: #player input loop
        print('Please enter your move: (r)ock (p)aper (s)cissors, or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # quit the program
        if playerMove == 'r'or playerMove == 'p' or playerMove == 's':
            break # break out of player input loop
        #secret code
        if playerMove == 'tiddy':
            print('(Hehe you found the easter egg... tiddy.)')
        print('Please develop some reading comprehension, Erica.')

    # display what the player chose
    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors versus ...')

    # display what the computer chose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('rock!')
    elif randomNumber == 2:
        computerMove = 'p'
        print('paper!')
    elif randomNumber == 3:
        computerMove = 's'
        print('scissors!')

    # display and record the win/loss/tie:

    #tie
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    #player wins
    elif playerMove == 'r' and computerMove == 's':
        print('You crush the scissors with your mighty rock and win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You cut the paper up with your spectacular scissors and you win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Your powerful paper wraps around the rock and you win!')
        wins = wins + 1
    #player loses
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose! The computer was smarter than you.')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose! The computer was smarter than you.')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose! The computer was smarter than you.')
        losses = losses + 1
