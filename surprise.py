from datetime import *

import os
import random
import time

DELAY = 0.5
CONGRATULATIONS_COUNT = 10000


def str_in_place(str, row, col):
    width, height = os.get_terminal_size()
    total = width * height
    before_spaces = row * width + col
    after_spaces = total - before_spaces - len(str)
    before_str = '\r' + before_spaces * ' '
    after_str = after_spaces * ' '
    return before_str + str + after_str


def add_snow(msg, ratio=0.01):
    char_list = list(msg)
    spaces_count = len([c for c in char_list if c == ' '])
    stars_count = int(spaces_count * ratio)
    while stars_count > 0:
        pos = random.randint(1, len(char_list) - 1)
        if char_list[pos] == ' ':
            char_list[pos] = '*'
            stars_count -= 1
    return ''.join(char_list)


def delta_to_str(delta):
    return str(delta).split('.')[0]


def show_progress(delta, total_delta):
    print('\rDima is coming in {} ... it is only {:.1f}% of total {}'.format(
        delta_to_str(delta),
        delta / total_delta * 100,
        delta_to_str(total_delta)
    ), end='', flush=True)


def show_congratulations():
    width, height = os.get_terminal_size()
    row = random.randint(0, min(height, 10))
    col = random.randint(0, min(width, 60))
    message = str_in_place("Dima is here!!!", row, col)
    message_with_stars = add_snow(message)
    print(message_with_stars, end='', flush=True)


departure_datetime = datetime(2018, 10, 27, 21, 20)
return_datetime = datetime(2018, 12, 1, 9, 10)


total_delta = return_datetime - departure_datetime
current_datetime = datetime.now()

while current_datetime < return_datetime:
    current_datetime = datetime.now()
    remaining_delta = return_datetime - current_datetime
    show_progress(remaining_delta, total_delta)
    time.sleep(DELAY)

for i in range(CONGRATULATIONS_COUNT):
    show_congratulations()
    time.sleep(DELAY)