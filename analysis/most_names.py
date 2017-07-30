import csv

from collections import Counter

'''
Counts the most called name of the simpsons family.
'''

with open('../total_count.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    count = dict(reader)

simpsons = [ 'marge', 'homer', 'bart', 'lisa', 'maggie', 'abraham', 'mona' ]

for c in simpsons:
    print(c, ':', count[c])

