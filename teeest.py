import re
# https://regex101.com/delete/Y2vrl6ugqjO92cnzZuYk5MjK8Cw9MpiVwY9u

my_test_arr = ['word -', 'word-', 'just ignore me', 'test- more elaborate text', 'test - yet another example',
               '- not this one', ' -nor this']

for index, test_str in enumerate(my_test_arr):
    #   Remove hyphen if exists, match only those in which exist.
    remove_hyphen = test_str.split('-')[0] if '-' in test_str else ''
    matching_string = re.match(r"\b{}(?= )?\b".format(remove_hyphen), test_str, re.IGNORECASE) if remove_hyphen else ''

    if matching_string:
        print(matching_string.group(), 'from my_test_arr index', index, 'matches.')

