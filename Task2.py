import csv

# Read data from files
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Dictionary to store total call duration per phone number
call_durations = {}

# Process each call
for call in calls:
    incoming, receiving, _, duration = call
    duration = int(duration)

    # Add duration for incoming number
    if incoming in call_durations:
        call_durations[incoming] += duration
    else:
        call_durations[incoming] = duration

    # Add duration for receiving number
    if receiving in call_durations:
        call_durations[receiving] += duration
    else:
        call_durations[receiving] = duration

# Find the phone number with the longest total call duration
max_number = max(call_durations, key=call_durations.get)
max_duration = call_durations[max_number]

# Print the result
print(f"{max_number} spent the longest time, {max_duration} seconds, on the phone during September 2016.")


"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

