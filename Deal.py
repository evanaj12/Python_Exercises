# File: Deal.py

# Description:Shows outcomes of 'Let's Make a Deal' game, AKA the Monty Hall problem,
# demonstrating the correctness of Marilyn vos Savant's prediction

# Student Name:Evan Johnston

# Student UT EID:eaj628

# Partner's Name:Carlos Ortiz

# Partner's UT EID:cbo628

# Course Name: CS 303E

# Unique Number:53590

# Date Created:10/10/13

# Date Last Modified:10/13/13

def main():

    num_games=int(input('Enter number of times you want to play: '))
    #read in number of games user wants to play
    print('')
    print('  Prize      Guess       View    New Guess')

    switch_wins=0
    #initialize number of wins after switching

    for i in range(1,num_games+1):
        #this loop repeats the game the number of times the user specified
        
        import random
        prize=random.randint(1,3)
        #prize is the number of the door the prize is behind

        guess=random.randint(1,3)
        #guess is the player's first guess

        view=random.randint(1,3)
        while view==guess or view==prize:
            view=random.randint(1,3)
        #view is the number of the door revealed; it cannot be
        #the guess or prize door
        
        newGuess=random.randint(1,3)
        while newGuess==guess or newGuess==view:
            newGuess=random.randint(1,3)
        #newGuess is the player's guess after the reveal; it cannot be
        #the previous guess or the revealed door

        if newGuess==prize:
            switch_wins=switch_wins+1
            #increments number of wins after switching

        print('   ',prize,'        ',guess,'        ',view,'        ',newGuess)

    print('')
    prob_switch=round(switch_wins/num_games,2)
    print ('Probability of winning if you switch =',prob_switch)
    #finds and returns probability of winning after switching door choice

    prob_no_switch=round(1-prob_switch,2)
    print ('Probability of winning if you do not switch =',prob_no_switch)
    #finds and returns probability of winning if player keeps door choice
           
main()
