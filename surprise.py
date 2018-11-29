from datetime import *

import os
import random
import time

DELAY = 0.5
CONGRADULATIONS_COUNT = 10000


def print_in_place(str, row, col):
    width, height = os.get_terminal_size()
    total = width * height
    before_spaces = row * width + col
    after_spaces = total - before_spaces - len(str)
    print('\r' + before_spaces * ' ', end='')
    print(str, end='')
    print(after_spaces * ' ', end='', flush=True)


def delta_to_str(delta):
    return str(delta).split('.')[0]


def show(delta, total_delta):
    print('\rDima is coming in {} ... it is only {:.1f}% of total {}'.format(
        delta_to_str(delta),
        delta / total_delta * 100,
        delta_to_str(total_delta)
    ), end='', flush=True)


def show_congradulations():
    width, height = os.get_terminal_size()
    row = random.randint(0, min(height, 10))
    col = random.randint(0, min(width, 60))
    print_in_place("Dima is here!!!", row, col)


departure_datetime = datetime(2018, 10, 27, 21, 20)
return_datetime = datetime(2018, 12, 1, 9, 10)

total_delta = return_datetime - departure_datetime
current_datetime = datetime.now()

while current_datetime < return_datetime:
    current_datetime = datetime.now()
    remaining_delta = return_datetime - current_datetime
    show(remaining_delta, total_delta)
    time.sleep(DELAY)

for i in range(CONGRADULATIONS_COUNT):
    show_congradulations()
    time.sleep(DELAY)