import codecs
import random

f = codecs.open('../stage1/elec_pairs_stage1.txt', 'r', errors='ignore')

lines = []

for line in f:
    line = unicode(line, errors='ignore')
    lines.append(line)

random.seed(12345678)
random.shuffle(lines)

fw = open("X.txt", 'w')

for i in range(0, len(lines) / 2):
    fw.write(lines[i])

fw.close()

fw = open("Y.txt", 'w')

for i in range(len(lines) / 2, len(lines)):
    fw.write(lines[i])

fw.close()
