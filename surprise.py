from datetime import *

import os
import random
import time

DELAY = 0.8
CONGRATULATIONS_COUNT = 10000
ERASE = '\x1b[1A\x1b[2K'


HAPPY_SUN = """
                                   KN.                                       
                                  .MMl                                       
                                   XM0                                       
                                   oMM.                                      
                                   .MMo      'l'                             
                        :Ol         0MN      NMO                ,dl          
                        ,WMk        cMM.    :MM;             .lNMNo          
    .:,                  .KMN,      .MMc    XMX            ;OMMO,            
    :XMMXkc'               lWMk.     MMd   ,MM:         .dNMXl.              
       'lkNMMKx:.           .OMW;    .,    .0O.      .cKMWx'                 
           .;o0WMW0d;.        ,c.   .;coxkkkxo:.   .KMMO:                    
                .:dKMMWOo;.     'dKXko:,....';lkN0l.;;                       
                     .cxKWk   oNO:.              .oN0,        .,cokXK.       
            .dl;'..         :Wk.  ...               cWO  :dOXMMMXOxl,        
            .xKNMMMMMMMWN. oM: .d0dllx0:             .XX,00dc'.              
                 ...'',,. ,Ml  d;      Xl   ;xOkkOk,  .Mk                    
                      .   OW           oK 'Xo.    .Nl  0W                    
         ..';:ldxOKNWMMN  XX                       'l  XN,:'.                
,ldxOKXWMMMMWX0Oxoc:,..   kM.    c.                   'Md0NMMMMWXKOkdol:;'.. 
d0kxol:,'.                .WO    Wc          .:      .N0    ..',:codkOKXNMMMX
                       .lOk;Wk   ,Nc       .oX;     ;Wk                    . 
                   .lOWMWk: .KX,   ckkxdxkOx;     '0N;.l:                    
               .cOWMWkc.      :XK:              :KXc  'KMWk,                 
              XMWOc.          '.,xN0o;..  ..;o0Nx'      .oNMNd.              
              .'           .oWMX   .;lxOOOOxl;cNK.         'xWMKc            
                         .kMMk'      ,NK       OMW.           :Ok.           
                       .OMMx.        lMM.       kMW,                         
                     .kMMx.          lMM.        xMM;                        
                   .xMMx.            oMM.         oMMc                       
                 .xMMk.              OMN           cMMl                      
                dWMO.                .c.            ;MMd                     
                co.                                  'WMk                    
                                                      ;Wd                                                                  
"""


def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')


def str_in_place(str, row, col):
    width, height = os.get_terminal_size()
    total = width * height
    before_spaces = row * width + col
    after_spaces = total - before_spaces - len(str)
    before_str = before_spaces * ' '
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


def get_progress_msg(delta, total):
    return 'Dima is coming in {} ... it is only {:.1f}% of total {}'.format(
        delta_to_str(delta),
        delta / total * 100,
        delta_to_str(total)
    )


def get_surprise_timer_msg(delta):
    return 'Time left to surprise: {} ... Please be at home in time (20:45)'.format(delta_to_str(delta))


def can_show_happy_sun(w, h):
    return w > 77 and h > 35


def get_surprise_msg():
    width, height = os.get_terminal_size()
    image_text = HAPPY_SUN if can_show_happy_sun(width, height) else ""
    return 'SURPRISE TIME!!! Please relax and enjoy. The surprise should appear soon.\n' + image_text


def print_messages(msgs):
    clear_screen()
    for msg in msgs:
        print(msg)


def show_congratulations():
    width, height = os.get_terminal_size()
    row = random.randint(0, height - 1)
    col = random.randint(0, width - 1)
    message = str_in_place("Dima is here!!!", row, col)
    message_with_stars = add_snow(message)
    clear_screen()
    print(message_with_stars)


departure_datetime = datetime(2018, 10, 27, 21, 20)
return_datetime = datetime(2018, 12, 1, 9, 10)
surprise_datetime = datetime(2018, 11, 30, 20, 45)
surprise_duration = timedelta(minutes=45)

total_delta = return_datetime - departure_datetime
current_datetime = datetime.now()

while current_datetime < return_datetime:
    current_datetime = datetime.now()
    remaining_delta = return_datetime - current_datetime
    messages = [get_progress_msg(remaining_delta, total_delta)]
    if current_datetime < surprise_datetime:
        messages.append(get_surprise_timer_msg(surprise_datetime - current_datetime))
    elif current_datetime < surprise_datetime + surprise_duration:
        messages.append(get_surprise_msg())
    print_messages(messages)
    time.sleep(DELAY)

for i in range(CONGRATULATIONS_COUNT):
    show_congratulations()
    time.sleep(DELAY)
