import time
from datetime import datetime
from main import Meaning
from main import Saving
from win10toast import ToastNotifier


def remind_me(hour, minute):
    toaster = ToastNotifier()
    while True:
        if datetime.now().hour > 12:
            hr = datetime.now().hour - 12
        else:
            hr = 12 - datetime.now().hour
        minu = datetime.now().minute
        print(hr, minu)
        if hr == hour and minu == minute:
            data = Meaning()
            toaster.show_toast("Daily Vocabs", data, duration=20)
            Saving()
            break
        else:
            time.sleep(60)


reminder_hour = int(input("Enter time(hr) you need a reminder(orignal Time): "))

reminder_minute = int(input("Enter time(min) you need a reminder(orignal Time): "))


# Call the function to start the reminder
remind_me(reminder_hour, reminder_minute)
