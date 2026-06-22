"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

with open("texts.csv", "r") as f:
    reader = csv.reader(f)
    texts = list(reader)

with open("calls.csv", "r") as f:
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

telephone_numbers = []
telephone_totals = []

for call in calls:
    duration = int(call[3])
    participants = [call[0], call[1]]

    for participant in participants:
        found_index = -1

        for index in range(len(telephone_numbers)):
            if telephone_numbers[index] == participant:
                found_index = index
                break

        if found_index == -1:
            telephone_numbers.append(participant)
            telephone_totals.append(duration)
        else:
            telephone_totals[found_index] = telephone_totals[found_index] + duration

longest_number = telephone_numbers[0]
longest_total = telephone_totals[0]

for index in range(1, len(telephone_numbers)):
    if telephone_totals[index] > longest_total:
        longest_total = telephone_totals[index]
        longest_number = telephone_numbers[index]

print(
    "{} spent the longest time, {} seconds, on the phone during September 2016.".format(
        longest_number, longest_total
    )
)
