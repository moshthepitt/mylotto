import csv
from collections import Counter

filename = "data/mylotto.csv"
data = []


def write_counter_to_file(the_data, the_file, header=[]):
    writer = csv.writer(open(the_file, 'w'))
    if header:
        writer.writerow(header)
    for row0 in the_data:
        writer.writerow([j for j in row0])


def last_won(the_data):
    when_filename = "results/date_numbers.csv"
    the_result = []
    for n in range(0, 50):
        for i, v in enumerate(the_data):
            if n in v['numbers']:
                the_result.append([n, i, v['date']])
                break
    the_result.sort(key=lambda x: x[1])
    write_counter_to_file(the_result, when_filename, ["Number", "Rank", "Date"])


def last_won_bonus(the_data):
    when_filename = "results/date_bonus_numbers.csv"
    the_result = []
    for n in range(0, 10):
        for i, v in enumerate(the_data):
            if n == v['bonus']:
                the_result.append([n, i, v['date']])
                break
    the_result.sort(key=lambda x: x[1])
    write_counter_to_file(the_result, when_filename, ["Number", "Rank", "Date"])


with open(filename, "rb") as ifile:
    reader = csv.reader(ifile)
    for row in reader:
        data.append(
            {
                'date': row[0],
                'jackpot': row[1],
                'numbers': [int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7])],
                'bonus': int(row[8]),
                'winners': row[9],
                'amount': row[10]
            }
        )

# common bonuss
bonus_filename = "results/bonus_numbers.csv"
bonus_numbers = Counter([z['bonus'] for z in data])
write_counter_to_file(bonus_numbers.most_common(), bonus_filename, ["Number", "Occurences"])

# common picks
numbers_filename = "results/numbers.csv"
numbers = Counter(sum([y['numbers'] for y in data], []))
write_counter_to_file(numbers.most_common(), numbers_filename, ["Number", "Occurences"])

# when last won
last_won(data)
last_won_bonus(data)
