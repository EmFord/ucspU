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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
call_set = set()
text_set = set()

text_set.update(record[0] for record in texts)
text_set.update(record[1] for record in texts)
call_set.update(record[0] for record in calls)
call_set.update(record[1] for record in calls)

count = text_set.union(call_set)
print(f"There are {len(count)} different telephone numbers in the records")