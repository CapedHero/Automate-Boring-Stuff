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

# TODO: Add passing number of quiz as parameters.
# TODO: Add dynamic leading zeroes, so the number of digits always equals max quiz number.
for quiz_num in range(1, 4):
    # Create the quiz and 'answer' key files.
    if not os.path.exists('tests'):
        os.makedirs('tests')
    if not os.path.exists('answers'):
        os.makedirs('answers')
    quiz_file = open('tests/capitals_quiz_%02d.txt' % quiz_num, 'w')
    quiz_answers = open('answers/capitals_quiz_%02d_answers.txt' % quiz_num, 'w')

    # Write out the header for the quiz.
    quiz_file.write('''
Name: 
Date:

                         State Capitals Quiz (Form {})
                              
    '''.format(quiz_num))

    questions = list(questions_and_answers.keys())
    random.shuffle(questions)

    # TODO: Loop through all 50 states, making a question for each.
