''' 
This module contains functions to load questions from a CSV file, 
choose random questions, and ask questions to the user.
'''

import csv
import random

def load_questions(csv_file):

    '''
    Function to load questions from a CSV file
        params: csv_file (str) - path to the CSV file

        returns: list of questions (list)

    The CSV file has the following format:
        question, option1, option2, option3, correct_option

    Example:

        trivia_questions.csv:
        question, option1, option2, option3, correct_option
        What is the capital of France?, New York, London, Paris, Paris
        What is the capital of Spain?, New York, London, Madrid, Madrid

        result = load_questions('trivia_questions.csv')

        result = [
            ["What is the capital of France?", "New York", "London", "Paris", "Paris"]
            ["What is the capital of Spain?", "New York", "London", "Madrid", "Madrid"]
        ]
    '''

    with open(csv_file, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader, None)  # Omitir la primera línea (títulos)
        csv_reader = filter(lambda x: len(x) == 5, csv_reader)
        return list(csv_reader)
    
def unique_random_generator(count, limit=18):

    '''
    Generator function that yields unique random numbers
        params: count (int) - number of random numbers to generate
                limit (int) - upper limit for the random numbers

        yields: random number (int)

    Example:
        gen = unique_random_generator(5, 10)

        for i in gen:
            print(i)

        Output:
        2
        3
        7
        1
        9

    '''
    seen = set()  
    while len(seen) < count:
        random_number = random.randint(0, limit)
        if random_number not in seen:
            seen.add(random_number)
            yield random_number

def choose_questions(questions):

    '''
    Function to choose 5 random questions from a list of questions
        params: questions (list) - list of questions

        returns: list of 5 questions (list)

    Example:
        questions = [
            ["What is the capital of France?", "New York", "London", "Paris", "Paris"]
            ["What is the capital of Spain?", "New York", "London", "Madrid", "Madrid"]
            ["What is the capital of Italy?", "New York", "Rome", "Paris", "Rome"]
            ["What is the capital of Germany?", "New York", "London", "Berlin", "Berlin"]
            ["What is the capital of England?", "New York", "London", "Paris", "London"]
            ["What is the capital of Portugal?", "New York", "Lisbon", "Paris", "Lisbon"]
            ["What is the capital of Belgium?", "New York", "London", "Brussels", "Brussels"]
            ["What is the capital of Netherlands?", "New York", "London", "Amsterdam", "Amsterdam"]
            ["What is the capital of Denmark?", "New York", "Copenhagen", "Paris", "Copenhagen"]
            ["What is the capital of Sweden?", "New York", "Stockholm", "Paris", "Stockholm"]
        ]

        result = choose_questions(questions)

        result = [
            ["What is the capital of France?", "New York", "London", "Paris", "Paris"]
            ["What is the capital of Spain?", "New York", "London", "Madrid", "Madrid"]
            ["What is the capital of Italy?", "New York", "Rome", "Paris", "Rome"]
            ["What is the capital of Germany?", "New York", "London", "Berlin", "Berlin"]
            ["What is the capital of England?", "New York", "London", "Paris", "London"]
        ]

    '''	
    indices = [i for i in unique_random_generator(5, len(questions) - 1)]
    return [questions[i] for i in indices]

def ask_question(question):

    '''
    Function to ask a question to the user
        params: question (list) - question and options

        returns: True if the user answered correctly, False otherwise
    
    Example:
        question = ["What is the capital of France?", "New York", "London", "Paris", "Paris"]

        result = ask_question(question)

        What is the capital of France?
        1. New York
        2. London
        3. Paris
        Your answer (1-3): 3
        Correct

        result = True
    '''
    print(question[0])
    
    for idx in range(1, 4):
        print(f"{idx}. {question[idx]}")
    
    while True:
        try:
            user_answer = int(input("Your answer (1-3): "))
            if user_answer in [1, 2, 3]:
                break
            else:
                print("Please enter a valid option: 1, 2, or 3.")
        except ValueError:
            print("Please enter a number.")

    isCorrect = question[user_answer] == question[4]

    if isCorrect:
        print('Correct')
    else:
        print('Incorrect, the correct answer is:', question[4])

    return isCorrect
    
