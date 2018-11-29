from datetime import *

import os
import random
import time

DELAY = 0.8
CONGRATULATIONS_COUNT = 10000
ERASE = '\x1b[1A\x1b[2K'


HAPPY_SUN = """
                                             ;NX.                                                   
                                             0MMx                                                   
                                             oMMX                                                   
                                             .MMM'                                                  
                                              0MMk                                                  
                                              ;MMM.        okl                                      
                               .xk:            WMMo       cMMW                      :o;             
                               'WMMd           xMMX       XMMx                   ;kMMMK             
                                .KMMX'         ;MMM.     cMMM.                .dWMMNo.              
     .KNOo;.                      lWMMx.       .MMM;     NMMx              .lXMMWx'                 
      o0WMMMWOo,.                  .OMMWc       NMM:    ,MMM.            :0MMM0:                    
         .;o0WMMMNOo;.               ,XMMX.      '.     .OXx          :OMMMKl.                      
              .;o0WMMMNOo;.            cxo       .,:cllolc:,.      c0MMMXo.                         
                   .;oONMMMW0d;.           .:x0WWXOkdollodk0NMKx:. oKOl.                            
                        .,oONMMMWKl     'xNWOl,.              ,oKMKl                  .',           
                             .,lxk:   :XMk,                      .lNWx.       ..;lxOXMMMM0          
                c0Odc;'...          .XMx.   .','.                   cWWc  lkKWMMMMWXOdl;.           
                c0NMMMMMMMMMMMMMx  ;WW'  'kNOdlokNk.                 .KMx'XN0xl;..                  
                    ..,;:clloool. .WW.  oWc       dM:     'lxOK0kl.    XMc                          
                                  OMd              KW   oN0c'   .oWx   :MX                          
                       ..';clo:   MM.              cx  oO.        ;Mo  'MM                          
          ..,:codk0KNWMMMMMMMMX.  MM.                              ,.  cMXlkdl:,'..                 
'odkOKXWMMMMMMMMWXKOxdlc;'..      0Mo      o'                          XMckNMMMMMMMMWNX0Okdol:;,... 
OWWXKOkdoc:,'.                    'MW.    .Mx              .'         0Md     ..,;cldxO0KNWMMMMMMMMK
                                ,c,:MN.    xM:            oWx       .KMo                     ..',;:.
                            ,o0MMMN.,NWl    ;KXl,.   .'ckNx.       dMX,                             
                       .:xXMMMNOl.    xMX:    .:dk000Odc'       .dWNc .KW0c                         
                   .:kNMMMXx:.         .xWNo.                 :0MK:    cKMMMO:                      
                  XMMMXd;.             .. :kWNkl,.      .':dKMXo.        .lXMMWk;                   
                  ,l;.              .oNMMd   .cd0XWMWWWMNKkooKO:            .oNMMWk,                
                                  'kMMMO;        co:        'WMMd              'dNMMk               
                                ;KMMWd.         ,MMM.        .XMMO                ''                
                              cNMMXc            ,MMM.         .KMMK.                                
                            lNMMK;              'MMM.           OMMN.                               
                          lWMMK,                ,MMM.            dMMW'                              
                        oWMM0,                  lMMW              cMMM:                             
                     .oWMM0'                    lMMo               ,WMMo                            
                    .WMMO'                                          .NMMk                           
                     ';.                                             .KMM0                          
                                                                       0Wc                          
"""


def clear_screen():
    width, height = os.get_terminal_size()
    print(ERASE * height)


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
    return w > 100 and h > 40


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