#!/usr/bin/env python3
#
# quiz_generator.py - Create quizzes along with answer keys.
#                     Questions and answers are in random order.

import os
import random


# Quiz test data. Keys are states and values are their capitals.
usa_capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinois': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Moines',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'Saint Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Nevada': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhode Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'
}

questions_and_answers = usa_capitals
quizzes_num = 14
questions_num = 50
options_num = 4
lead_zeros = len(str(quizzes_num))
if not os.path.exists('tests'): os.makedirs('tests')
if not os.path.exists('answers'): os.makedirs('answers')

for quiz_no in range(1, quizzes_num + 1):
    # Create quiz and answer key files.
    quiz_no = str(quiz_no)

    path_quiz = 'tests' + os.sep + 'capitals_quiz_' + quiz_no.zfill(lead_zeros) + '.txt'
    quiz_file = open(path_quiz, 'w')

    path_answers = 'answers' + os.sep + 'capitals_quiz_' + quiz_no.zfill(lead_zeros) + \
                   '_answers.txt'
    answers_file = open(path_answers, 'w')

    # Write the header.
    quiz_file.write('''
Name: 
Date:


STATE CAPITALS QUIZ (Form {})
           
                              
'''.format(quiz_no))

    # Write questions and answers.
    questions = list(questions_and_answers.keys())
    random.shuffle(questions)

    for question_no in range(1, questions_num + 1):
        question = questions[question_no - 1]
        correct_answer = questions_and_answers[question]

        wrong_answers = list(questions_and_answers.values())
        wrong_answers.remove(correct_answer)
        wrong_answers = random.sample(wrong_answers, options_num - 1)

        all_answers = wrong_answers + [correct_answer]
        random.shuffle(all_answers)

        quiz_file.write('%d. What is the capital of %s\n' % (question_no, question))
        for i in range(options_num):
            quiz_file.write('\t%s. %s\n' % ('ABCD'[i], all_answers[i]))
        quiz_file.write('\n')
        
        answers_file.write('%s. %s\n' % (question_no, correct_answer))

    quiz_file.close()
    answers_file.close()
