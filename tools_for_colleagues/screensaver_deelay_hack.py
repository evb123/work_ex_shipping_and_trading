import pyautogui as pag
import time
import datetime as dt

if __name__ == '__main__':
    print('\n')
    print('--------------------------------------------------------------------------------------')
    print('Working :)')
    print('\n')
    print('This program moves the cursor by one pixel every 9.5 minutes to delay the screensaver.')
    print('It will automatically quit at 17h.')
    print('Press Ctrl-C to quit at anytime.')
    print('\n')
    print('--------------------------------------------------------------------------------------')

    while 'shipping' == 'shipping' and dt.datetime.today().hour != 17:
        if pag.position()[1] != 0:
            pag.move(0, -1)
            time.sleep(60*9.5)
        else:
            while pag.position()[1] != pag.size()[1]:
                pag.move(0, 1)
                time.sleep(60*9.5)
    quit()

