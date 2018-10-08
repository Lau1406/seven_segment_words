import re
from src import constants


def main():
    with open(constants.filename, 'r') as file:
        # Get the words as an array
        words = file.read().split('\n')

        # Get the regex
        r = re.compile(constants.regex_banned_letters, re.IGNORECASE)

        # Process the list
        passed_words = list(filter(r.match, words))


if __name__ == '__main__':
    main()
