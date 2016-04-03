import codecs

f = codecs.open('../stage1/elec_pairs_stage1.txt', 'r', errors='ignore')

lines = []

for line in f:
    line = unicode(line, errors='ignore')
    lines.append(line)

print len(lines)
