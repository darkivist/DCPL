#this actually runs, but does not find any matches. What's the problem here???
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import csv

save_file = open('FuzzyResults3.csv', 'w')
writer = csv.writer(save_file, lineterminator = '\n')

def parse_csv(path):

    with open(path,'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            yield row


if __name__ == "__main__":
    data = []
    for row in parse_csv('HSW.csv'):
        data.append(row[0])

    print "%d candidates at HSW" % (len(data))

    ## For each row in the lookup compute the partial ratio
    for row in parse_csv("WASH.csv"):
        title = row[0]

        output_row = [title]

        matches = []
        for candidate in data:
            score = fuzz.ratio(title, candidate)
            matches.append((score, candidate))
        matches = sorted(matches, key=lambda x: x[0])
        best_match = matches[-1]
        print "Best strict match for %s is %s (score: %d)" % (title, best_match[1], best_match[0])
        output_row.append(best_match[1])
        output_row.append(best_match[0])

        matches = []
        for candidate in data:
            score = fuzz.partial_ratio(title, candidate)
            matches.append((score, candidate))
        matches = sorted(matches, key=lambda x: x[0])
        best_match = matches[-1]
        print "Best partial match for %s is %s (score: %d)" % (title, best_match[1], best_match[0])
        output_row.append(best_match[1])
        output_row.append(best_match[0])

        writer.writerow(output_row)

save_file.close()
