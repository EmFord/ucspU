"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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

outgoing_calls = set()
incoming_calls = set()
outgoing_texts = set()
incoming_texts = set()
for record in calls:
    outgoing_calls.add(record[0])
    incoming_calls.add(record[1])

for record in texts:
    outgoing_texts.add(record[0])
    incoming_texts.add(record[1])

calls_exc = outgoing_calls.difference(incoming_calls)
calls_exc_minus_incoming = calls_exc.difference(incoming_texts)
telemarketers = calls_exc_minus_incoming.difference(outgoing_texts)
telemarketers = sorted(telemarketers)
build_string = '\n'.join(telemarketers)

print(f"These numbers could be telemarketers: \n{build_string}")
