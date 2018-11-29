# from tqdm import tqdm
from datetime import *
import sys
import time


def show(delta, total_delta):
    print('\rDima is coming in ', end='')
    print(str(delta).split('.')[0], end='')
    print(' ... {:.1f}%'.format(delta / total_delta * 100), end='')
    sys.stdout.flush()


departure_datetime = datetime(2018, 10, 27, 21, 20)
return_datetime = datetime(2018, 12, 1, 9, 10)

total_delta = return_datetime - departure_datetime
current_datetime = datetime.now()

while current_datetime < return_datetime:
    current_datetime = datetime.now()
    remaining_delta = return_datetime - current_datetime
    show(remaining_delta, total_delta)
    time.sleep(1)