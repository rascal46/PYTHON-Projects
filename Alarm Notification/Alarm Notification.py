from plyer import notification
import time
from datetime import datetime

def wait_until(target_time_str):
    # Format should be "HH:MM" in 24-hour format
    now = datetime.now()


    target_time = datetime.strptime(target_time_str, "%H:%M").replace(
        year=now.year, month=now.month, day=now.day
    )

    # If target time already passed today, assume it's for the next day
    if target_time < now:
        target_time = target_time.replace(day=now.day + 1)

    seconds_until = (target_time - now).total_seconds()
    print(f"Waiting for {int(seconds_until)} seconds...")
    time.sleep(seconds_until)

def set_reminder_at_time(title, message, time_str):
    wait_until(time_str)
    notification.notify(
        title=title,
        message=message,
        timeout=10
    )

now = datetime.now()
print(f"Current time: {now.strftime('%H:%M')}")

print("Input in 24-hour format (HH:MM)")

a = input("Enter the title of the reminder: ")

if not a:
    print("No title entered. Exiting.")
    exit()  


b = input("Enter the message of the reminder: ")

if not b:
    print("No message entered. Exiting.")
    exit()


title = a
message = b

x = input("Enter the time for the reminder (HH:MM): ")

if not x:
    print("No time entered. Exiting.")
    exit()

target_time = x

set_reminder_at_time(title, message, target_time)
print("Reminder set!")

