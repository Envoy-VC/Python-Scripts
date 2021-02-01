import time
import os
from win10toast import ToastNotifier
toaster = ToastNotifier()
birthdayFile = 'birthdays'


def checkTodaysBirthdays():
    fileName = open(birthdayFile, 'r')
    today = time.strftime('%m%d')
    flag = 0
    notification_body = ''
    bday_list =[]
    for line in fileName:
        if today in line:
            line = line.split(' ')
            msg = line[1] + ' ' + line[2]
            bday_list.append(msg)
            flag = 1
    for names in bday_list:
        notification_body = notification_body + names
    toaster.show_toast("Birthdays Reminder -", notification_body, duration=20,icon_path='icon.ico')

    if flag == 0:
        toaster.show_toast("Birthdays Reminder -", "No Birthdays Today", duration=20,icon_path='icon.ico')


if __name__ == '__main__':
    checkTodaysBirthdays()