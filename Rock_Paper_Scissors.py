#===========================================================================
#Program:	Rock, Paper, Scissors
#Programmer:	Elizabeth Byrne
#Date: 		06/25/2021
#Abstract:	This program takes a player's choice and compares it to
#               a random computer choice and displays the winner of the
#               popular game 'Rock, Paper, Scissors'
#============================================================================
import random
def main():
	play_again = 'y'
	number_of_tied_games = 0
	number_of_players_games = 0
	number_of_computer_games = 0
	print("Let's play the game of Rock, Paper, Scissors.")
	while play_again == 'y' or play_again == 'Y':
		computer_choice = process_computer_choice()
		player_choice = process_player_choice()
		
                #display computer choice
		if computer_choice == 1:
			print('The computer chooses rock.')
		elif computer_choice == 2:
			print('The computer chooses paper.')
		else:
			print('The computer chooses scissors.')
			
		#display player choice
		if player_choice == 1:
			print('You chose rock.')
		elif player_choice == 2:
			print('You chose paper.')
		else:
			print('You chose scissors.')
			
		#display result	
		result = determine_winner(player_choice, computer_choice)
		if result == 'computer':
			number_of_computer_games += 1
		elif result == 'player':
			number_of_players_games += 1
		else:
			number_of_tied_games += 1
		print
		play_again = input('Do you want to play again? (Enter y for yes): ')
		print('There were', number_of_tied_games, 'tie games played. ')
		print('The computer won', number_of_players_games, 'game(s). ')
		print('You won', number_of_players_games, 'game(s). ')
		
def process_computer_choice():
        choice1 = random.randint(1, 3)
        return choice1
        
def process_player_choice():
        print('What is your choice? Enter 1 for rock, 2 for paper, or 3 for scissors: ',) 
        
        try:
                choice2 = int(input())    
                while choice2 != 1 and choice2 != 2 and choice2 != 3:
                    choice2 = int(input('ERROR: the choice can only be 1, 2, or 3.'))
                
                return choice2
        
        except ValueError:
                print('ERROR: the choice can only be 1, 2, or 3.')
                process_player_choice()
        
def determine_winner(player_choice, computer_choice):
        if computer_choice == 1:
            if player_choice == 2:
                print('Paper covers rock. You win!')
                winner = 'player'
            elif player_choice == 3:
                print('Rock crushes scissors. The computer wins!')
                winner = 'computer'
            else:
                print('The game is tied. Try again.')
                winner = 'tied'
         
        if computer_choice == 2:
            if player_choice == 1:
                print('Paper covers rock. The computer wins!')
                winner = 'computer'
            elif player_choice == 3:
                print('Scissors cuts paper. you win!')
                winner = 'player'
            else:
                print('The game is tied. Try again.')
                winner = 'tied'
                
        if computer_choice == 3:
            if player_choice == 1:
                print('Rock smashes scissors. You win!')
                winner = 'player'
            elif player_choice == 2:
                print('Scissors cut paper. The computer wins!')
                winner = 'computer'
            else:
                print('The game is tied. Try again?')
                winner = 'tied'
            return winner
main()
