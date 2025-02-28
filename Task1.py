import csv

# Read texts.csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

# Read calls.csv
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Using a set to store unique phone numbers
unique_numbers = set()

# Extract numbers from calls
for call in calls:
    incoming_call, answering_call = call[:2]  # First two elements
    unique_numbers.add(incoming_call)
    unique_numbers.add(answering_call)

# Extract numbers from texts
for text in texts:
    incoming_text, answering_text = text[:2]  # First two elements
    unique_numbers.add(incoming_text)
    unique_numbers.add(answering_text)

# Print the count of unique numbers
print(f"There are {len(unique_numbers)} different telephone numbers in the records.")

