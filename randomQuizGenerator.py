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

def generateQuiz(capitals, quizes_number):
    for quiz_number in quizes_number:
        generateQuizfile(quiz_number)
        for question_number in len(capitals):
            generateQuestion(capitals, question_number)
            appendAnswerfile(quiz_number, answer)
        
def generateQuizfile(quiz_number):
    with open (f'capitals_quiz{quiz_number + 1}.txt', 'a') as quiz_file:
        quiz_file.write('Name:\n\nDate:\n\n:Group:\n\n')
        quiz_file.write((' ' * 20) + f'State capitals Quiz (Form{quiz_number + 1})\n\n')

def appendQuizFile(capitals, quiz_number, question):
    with open (f'capitals_quiz{quiz_number + 1}.txt', 'a') as quiz_file:
        quiz_file.write(f'What is the capital of {capitals}')

def appendAnswerfile(quiz_number, answer):
    with open(f'capitals_quiz_answers{quiz_number +1}.txt', 'a') as answers_file:
        answers_file.write(f'{quiz_number}. {answer}\n')
        
        
def generateQuestion(capitals, question_number):
    states = list(capitals.keys()) 
    correct_answer = capitals[states[question_number]]
    wrong_answers = list(capitals.values())
    del wrong_answers[wrong_answers.index(correct_answer)]
    wrong_answers = random.sample(wrong_answers, 3)
    answer_options = wrong_answers + [correct_answer]
    random.shuffle(answer_options)
    question = f'What is the capital of {capitals.key(correct_answer)}?\n'
    return answer_options

    
    
def loadAnswers(file_path):
    with open(file_path) as input_file:
        lines = input_file.readlines()
        lines = [line.strip() for line in lines]
        string_answers = ' '.join(lines)
        answers = ast.literal_eval(string_answers) 
        return answers


if __name__ == '__main__':
    answers = loadAnswers(Path.cwd() / 'capitals.txt')
    #print(answers)
    print(generateQuestion(answers, 0))