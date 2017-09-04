#!/usr/bin/env python3
#
# quiz_generator.py - Create quizzes along with answer keys.
#                     Questions and answers are in random order.

import os
import random


def quiz_gen(data_set, quizzes_num=10, questions_num=10, options_num=4):
    lead_zeros = len(str(quizzes_num))
    if not os.path.exists('tests'): os.makedirs('tests')
    if not os.path.exists('answers'): os.makedirs('answers')

    for quiz_no in range(1, quizzes_num + 1):
        # Create quiz and answer key files.
        quiz_no_padded = str(quiz_no).zfill(lead_zeros)
        quiz_name = 'capitals_quiz_' + quiz_no_padded

        path_quiz = os.path.join('tests', (quiz_name + '.txt'))
        quiz_file = open(path_quiz, 'w')

        path_answers = os.path.join('answers', (quiz_name + '_answers.txt'))
        answers_file = open(path_answers, 'w')

        # Write the header.
        quiz_file.write('''
Name: 
Date:


{} (Form {})
               
                                  
'''.format('STATE CAPITALS QUIZ', quiz_no_padded))

        # Write questions and answers.
        questions = list(data_set.keys())
        random.shuffle(questions)

        for question_no in range(1, questions_num + 1):
            question = questions[question_no - 1]
            correct_answer = data_set[question]

            wrong_answers = list(data_set.values())
            wrong_answers.remove(correct_answer)
            wrong_answers = random.sample(wrong_answers, options_num - 1)

            all_answers = wrong_answers + [correct_answer]
            random.shuffle(all_answers)

            quiz_file.write('%d. What is the capital of %s?\n' % (question_no, question))
            for i in range(options_num):
                quiz_file.write('\t%s. %s\n' % ('ABCD'[i], all_answers[i]))
            quiz_file.write('\n')

            answers_file.write('%s. %s\n' % (question_no, correct_answer))

        quiz_file.close()
        answers_file.close()
