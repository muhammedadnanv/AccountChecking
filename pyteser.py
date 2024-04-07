import datetime
import time

def set_alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time's up! Alarm activated at", alarm_time)
            break
        time.sleep(1)

def main():
    print("Welcome to the Time Alarm Tracker")
    print("Please enter the time for the alarm (HH:MM:SS format):")
    alarm_time = input()

    try:
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    except ValueError:
        print("Invalid time format. Please use HH:MM:SS")
        return

    print("Alarm set for", alarm_time)
    set_alarm(alarm_time)

if __name__ == "__main__":
    main()
