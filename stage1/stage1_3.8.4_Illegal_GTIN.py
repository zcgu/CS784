import json
import codecs

f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')

atttibute_name = u'GTIN'

count = 0

list = []

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2

    if atttibute_name in json1:
        if len(json1[atttibute_name][0]) != 14:
            print line_split[1] + ',' + json1[atttibute_name][0]
            list.append((line_split[1], json1[atttibute_name][0]))
            count += 1

    if atttibute_name in json2:
        if len(json1[atttibute_name][0]) != 14:
            print line_split[3] + ',' + json1[atttibute_name][0]
            list.append((line_split[3], json1[atttibute_name][0]))
            count += 1

print count
print list