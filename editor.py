def merge_rows(number_of_rows, is_ordered):
    string = ''
    for i in range(1, number_of_rows+1):
        row = input(f'- Row #{i}: ')
        if is_ordered:
            string += f'{i}. {row}\n'
        else:
            string += f'* {row}\n'
    return string


supported_formatters = [
    'plain',
    'bold',
    'italic',
    'link',
    'inline-code',
    'header',
    'line-break',
    'ordered-list',
    'unordered-list'
]

CHOOSE_FORMATTER = '- Choose a formatter:'
UNKNOWN_FORMAT_TYPE = 'Unknown formatting type or command. Please try again'
SPECIAL_COMMANDS = 'Special commands: !help !done'
TEXT = '- Text: '
LEVEL = '- Level: '
LABEL = '- Label: '
URL = '- URL: '
NUMBER_OF_ROWS = '- Number of rows: '

HELP_COMMAND = '!help'
DONE_COMMAND = '!done'
result_string = ''

while True:
    command = input(CHOOSE_FORMATTER)
    if command == HELP_COMMAND:
        print('Available formatters:', ' '.join(supported_formatters))
        print(SPECIAL_COMMANDS)
    elif command == DONE_COMMAND:
        f = open('output.md', 'w')
        f.write(result_string)
        f.close()
        break
    elif command in supported_formatters:
        if command == supported_formatters[0]:
            text = input(TEXT)
            result_string += text
        elif command == supported_formatters[1]:
            text = input(TEXT)
            result_string += f'**{text}**'
        elif command == supported_formatters[2]:
            text = input(TEXT)
            result_string += f'*{text}*'
        elif command == supported_formatters[3]:
            label = input(LABEL)
            url = input(URL)
            result_string += f'[{label}]({url})'
        elif command == supported_formatters[4]:
            text = input(TEXT)
            result_string += f'`{text}`'
        elif command == supported_formatters[5]:
            level = int(input(LEVEL))
            text = input(TEXT)
            grids = '#' * level
            result_string += f'{grids} {text}\n'
        elif command == supported_formatters[6]:
            result_string += '\n'
        elif command == supported_formatters[7]:
            while True:
                rows = int(input(NUMBER_OF_ROWS))
                if rows < 1:
                    print('The number of rows should be greater than zero')
                else:
                    result_string += merge_rows(rows, True)
                    break
        elif command == supported_formatters[8]:
            while True:
                rows = int(input(NUMBER_OF_ROWS))
                if rows < 1:
                    print('The number of rows should be greater than zero')
                else:
                    result_string += merge_rows(rows, False)
                    break
        print(result_string)
    else:
        print(UNKNOWN_FORMAT_TYPE)
