#!/usr/bin/env python3
#
# quiz_generator.py - Create quizzes along with answer keys.
#                     Questions and answers are in random order.

import os
import random


# The quiz test data. Keys are states and values are their capitals.x
test_data = {
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

questions_and_answers = test_data
quizzes_num = 14
questions_num = 50
lead_zeros = len(str(quizzes_num))
if not os.path.exists('tests'): os.makedirs('tests')
if not os.path.exists('answers'): os.makedirs('answers')

for quiz_no in range(1, quizzes_num + 1):
    # Create the quiz and 'answer' key files.
    quiz_no = str(quiz_no)

    path_quiz = 'tests' + os.sep + 'capitals_quiz_' + quiz_no.zfill(lead_zeros) + '.txt'
    quiz_file = open(path_quiz, 'w')

    path_answers = 'answers' + os.sep + 'capitals_quiz_' + quiz_no.zfill(lead_zeros) + \
                   '_answers.txt'
    quiz_answers = open(path_answers, 'w')

    # Write the header.
    quiz_file.write('''
Name: 
Date:

                         State Capitals Quiz (Form {})
                              
    '''.format(quiz_no))

    questions = list(questions_and_answers.keys())
    random.shuffle(questions)

    # Write questions.
    for question_no in range(1, questions_num + 1):
        question = questions[question_no - 1]
        correct_answer = questions_and_answers[question]

        wrong_answers = list(questions_and_answers.values())
        del wrong_answers[wrong_answers.index(correct_answer)]
        wrong_answers = random.sample(wrong_answers, 3)

        all_answers = wrong_answers + correct_answer
        random.shuffle(all_answers)

        # TODO: Write the question and answer options to the quiz file.
        # TODO: Write the answer key to a file.
