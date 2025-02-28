import csv

# Read texts.csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# Read calls.csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Extract the first text record
first_text = texts[0]
incoming_text_number, answering_text_number, text_time = first_text

# Extract the last call record
last_call = calls[-1]
incoming_call_number, answering_call_number, call_time, call_duration = last_call

# Print the results
print(f"First record of texts, {incoming_text_number} texts {answering_text_number} at time {text_time}")
print(f"Last record of calls, {incoming_call_number} calls {answering_call_number} at time {call_time}, lasting {call_duration} seconds")

