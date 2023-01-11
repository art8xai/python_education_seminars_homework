# Initial file data for logging user input.
path_file = r'database/log.txt'


def log_file(update, expression_src, expression_res) -> None:
    """Write logs from the user to a file."""
    with open(path_file, 'a', encoding='UTF-8') as file:
        file.write('id=' + str(update.effective_chat.id) + ', input: ' + ''.join(map(str, expression_src))
                   + ', result: ' + str(expression_res) + ';\n')
