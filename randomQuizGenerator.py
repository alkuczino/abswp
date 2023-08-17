   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.
   
import random
from pathlib import Path
import os
import pprint
import ast 

#def saveQuiz():
    ###TODO
###
#def generateQuiz():
    ###TODO

#def generateQuestion(answers):
    ###TODO

def loadAnswers(file_path):
    with open(file_path) as input_file:
        lines = input_file.readlines()
        lines = [line.strip() for line in lines]
        string_answers = ' '.join(lines)
        answers = ast.literal_eval(string_answers) 
        return answers


if __name__ == '__main__':
    answers = loadAnswers(Path.cwd() / 'capitals.txt')
    print(answers)