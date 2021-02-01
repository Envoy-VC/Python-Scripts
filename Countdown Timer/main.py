import time
from playsound import playsound

def countdown(t):

    min_sec = input_time.split(sep=':')
    time_in_sec = (int(min_sec[0]) * 60) + int(min_sec[1])
    while time_in_sec:
        mins, secs = divmod(time_in_sec,60)
        timer = f"{mins}:{secs}"
        print('\r', timer, end="")
        time.sleep(1)
        time_in_sec -= 1

    playsound('audio.wav')

input_time = input(print("Enter Time (MM:SS) - "))
countdown(input_time)