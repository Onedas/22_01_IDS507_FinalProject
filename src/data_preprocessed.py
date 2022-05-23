import os
import re
from typing import List, Callable


def preprocess_data(file_name: str,
                    save_file_name: str,
                    functions: List[Callable] = None) -> None:
    """
        read file and replace the text lines through functions.
    """

    with open(file_name, 'r', encoding='cp949') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            for func in functions:
                line = func(line)
            new_lines.append(line)

    if save_file_name is not None:
        with open(save_file_name, 'w', encoding='cp949') as f:
            f.writelines(new_lines)
    return new_lines


def remove_tap(text):
    return text.replace('\t','')


def remove_space(text):
    return text.strip()


def remove_symbol(text): # except ',' symbol
    return re.sub('[^A-Za-z0-9가-힣,.-]', '', text)


def add_enter(text):
    return text + '\n'


if __name__ == '__main__':
    data_dir = '../data'
    for file_name in ['Humidity', 'Precipitation', 'Sunshine', 'Temperatures', 'Wind']:
        preprocess_data(f'{data_dir}/Original/{file_name}.csv', f'{data_dir}/{file_name}.csv', [remove_tap,
                                                                                                remove_space,
                                                                                                remove_symbol,
                                                                                                add_enter]
                        )