import csv

'''
This file is just to filter out the stop words.
'''

# get stop words
# list copied from here: http://www.lextek.com/manuals/onix/stopwords1.html
with open('stopwords_list.txt', 'r') as stop_file:
    stop_words = stop_file.read()
    stop_words = stop_words.split('\n')

# get all words
with open('total_count.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    mydict = dict(reader)

# write to new csv
with open('final_stop.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in mydict.items():
        # filter
        if key not in stop_words:
            writer.writerow([key, value])
