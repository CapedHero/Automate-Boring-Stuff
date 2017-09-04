#!/usr/bin/env python3
#
# phone_email_from_clipboard.py - Finds phone numbers and email addresses in clipboard text.

import re
import pyperclip

phone_regex = re.compile(r'''(
    (\(?\d{3}\)?)?                  # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)?                      # separator
    (\d{4})                         # first 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+]+    #username
    @
    [a-zA-Z0-9.-]+      # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
    )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []

# Append phone number in a standard format.
for phone_number in phone_regex.findall(text):
    phone_std = '-'.join([phone_number[1], phone_number[3], phone_number[5]])
    if phone_number[8] != '':
        phone_std += ' x' + phone_number[8]
    matches.append(phone_std)

# Append email.
for email in email_regex.findall(text):
    matches.append(email[0])

# Copy results to the clipboard.
if matches:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
