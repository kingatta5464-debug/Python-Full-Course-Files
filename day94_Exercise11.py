import time
import winsound
from plyer import notification

try:
    while True:
        time.sleep(2)
        # winsound.Beep(1000, 400)
        # print("💧 Time to drink water!") #for just a beep we can use this line of cod
        notification.notify(  # for a notification to be shown on desktop your PC you have to use this line of code
            title="Water Reminder", message="💧 Time to drink water!", timeout=2
        )


except KeyboardInterrupt:
    print("Keyboard interruption occured \n Good Bye!")
