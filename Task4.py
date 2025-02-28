import csv

# Read CSV files
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Use sets for efficiency
allReceivingNumbers = set()
uniqueCallingNumbers = set()

# Add receiving call numbers and text senders/receivers to allReceivingNumbers
for call in calls:
    allReceivingNumbers.add(call[1])

for text in texts:
    allReceivingNumbers.add(text[0])  # Sender of text
    allReceivingNumbers.add(text[1])  # Receiver of text

# Find telemarketers: numbers that only make outgoing calls
for call in calls:
    if call[0] not in allReceivingNumbers:
        uniqueCallingNumbers.add(call[0])

# Print sorted results
print("These numbers could be telemarketers: ")
for number in sorted(uniqueCallingNumbers):  # Sort lexicographically
    print(number)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

