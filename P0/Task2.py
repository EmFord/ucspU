"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

call_record = {}
for record in calls:
    if record[0] not in call_record.keys():
        call_record[record[0]] = int(record[-1])
    else:
        call_record[record[0]] += int(record[-1])

    if record[1] not in call_record.keys():
        call_record[record[1]] = int(record[-1])
    else:
        call_record[record[1]] += int(record[-1])

total_time = sorted(call_record.values())
total_time = total_time[-1]

call_record = {v: k for k, v in call_record.items()}
longest_number = call_record[total_time]

print(f"{longest_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")