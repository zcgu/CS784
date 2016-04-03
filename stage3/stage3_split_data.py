import codecs
import random
import stage3_helper

lines = stage3_helper.read_file('../stage1/elec_pairs_stage1.txt')

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
