   #! python3
   # randomQuizGenerator.py - Creates quizzes with questions and answers in
   # random order, along with the answer key.
   
import random
from pathlib import Path
import ast 


def generateQuiz(input_capitals, quizes_number):
    for quiz_number in range(quizes_number):
        generateQuizFile(quiz_number)
        generateAnswersFile(quiz_number)
        capitals = {k: input_capitals[k] for k in random.sample(list(input_capitals.keys()), len(input_capitals))}
        question_number = 1
        for state, capital in capitals.items():
            answers = generateAnswers(capitals, capital)
            str_answers = '\n'.join(['. '.join(text) for text in answers])
            answer = '\n'.join(['. '.join(text[0]) for text in answers if capital in text])
            appendQuizFile(quiz_number, f'{question_number}. What is the capital of {state}?\n\n{str_answers}\n\n')
            appendAnswersFile(quiz_number, f'{question_number}. {answer}\n')
            question_number += 1
        
def generateQuizFile(quiz_number):
    with open (f'capitals_quiz{quiz_number + 1}.txt', 'w') as quiz_file:
        quiz_file.write('Name:\n\nDate:\n\nGroup:\n\n')
        quiz_file.write((' ' * 20) + f'State capitals Quiz (Form {quiz_number + 1})\n\n')
        
def generateAnswersFile(quiz_number):
    with open(f'capitals_quiz_answers{quiz_number + 1}.txt', 'w') as answers_file:
        answers_file.write(f'Answers for quiz number {quiz_number + 1}\n')
        
def appendQuizFile(quiz_number, text):
    with open (f'capitals_quiz{quiz_number + 1}.txt', 'a') as quiz_file:
        quiz_file.write(f'{text}')

def appendAnswersFile(quiz_number, text):
    with open(f'capitals_quiz_answers{quiz_number + 1}.txt', 'a') as answers_file:
        answers_file.write(f'{text}')
        
def generateAnswers(capitals, correct_answer):
    letters = ['A', 'B', 'C', 'D']
    all_answers = list(capitals.values())
    del all_answers[all_answers.index(correct_answer)]
    all_answers = random.sample(all_answers, 3)
    all_answers.append(correct_answer)
    random.shuffle(all_answers)
    answers = [(letter, answer) for (letter, answer) in zip(letters, all_answers)]
    return answers

    
def loadAnswers(file_path):
    with open(file_path) as input_file:
        lines = input_file.readlines()
        lines = [line.strip() for line in lines]
        string_answers = ' '.join(lines)
        answers = ast.literal_eval(string_answers) 
        return answers


if __name__ == '__main__':
    input_capitals = loadAnswers(Path.cwd() / 'capitals.txt')
    generateQuiz(input_capitals, 35)