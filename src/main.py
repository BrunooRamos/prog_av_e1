'''
This is the main file of the trivia game.
It imports the necessary functions from the functions.py file and the List class from the list_monad.py file.
'''

from functions import load_questions, choose_questions, ask_question
from list_monad import List
from functools import reduce

def play_trivia():

    '''
    This function is the main function of the trivia game.
    It loads the questions from the csv file, selects 5 random questions, 
    asks them to the user and prints the final score.
    Este es el trabajo de trivia
    '''

    results = List(load_questions('trivia_questions.csv')).bind(choose_questions).bind(lambda selected_questions: map(ask_question, selected_questions)).value
    
    score = reduce(lambda acc, x: acc + (10 if x else 0), results, 0)
    print(f"Your final score is: {score}")
    
    if input("Play again? (yes/no): ").lower() == 'yes':
        play_trivia()

if __name__ == "__main__":
    play_trivia()
