import json
import codecs

f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')

PairIDlist = []

count = 0

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    if line_split[0] in PairIDlist:
        print line_split[0]
        count += 1
    else:
        PairIDlist.append(line_split[0])

if count == 0:
    print 'no duplicate PairID'

