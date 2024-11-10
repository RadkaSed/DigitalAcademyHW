import json


def count_letters(text):
    letters = {}
    for char in text:
        char = char.lower()
        if char != ' ' and char != '\n':
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    return letters



with open('alice.txt', mode='r', encoding='UTF-8') as input_file:
    result = count_letters(text=input_file.read())
    sorted_result = dict(sorted(result.items()))


with open('hw01_output.json', mode='w', encoding='UTF-8') as output_file:
    json.dump(sorted_result, output_file, ensure_ascii=False, indent=4)
