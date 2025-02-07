import re

path_to_file = "books/frankenstein.txt"


# Read File
def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    report = create_report(file_contents)
    print(report)


def count_words(file_content):
    cleaned_file_content = re.sub(r'\s+', ' ', file_content).strip()
    word_count = len(cleaned_file_content.split(" "))
    # print(word_count)

    return word_count


def count_chars(file_content):
    char_count = {}

    # cleaned_file_content = re.sub(r'\s+', ' ', file_content).strip()
    lower_file_content = file_content.lower()

    for char in lower_file_content:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


def create_report(file_content):
    report_str = '--- Begin report of books/frankenstein.txt ---'

    word_count = count_words(file_content)
    char_count = count_chars(file_content)

    report_str = f'''{report_str}
{word_count} words found in the document
'''

    for char in char_count:
        # print(char)
        if char.isalpha():
            report_str = f'''{report_str}
The '{char}' character was found {char_count[char]} times'''

    report_str = f'''{report_str}
--- End report ---'''

    return report_str

main()
