import json
import codecs

f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')

ProductIDlist = []
duplicate_list = []

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    if line_split[1] in ProductIDlist:
        duplicate_list.append(line_split[1])
    else:
        ProductIDlist.append(line_split[1])

    if line_split[3] in ProductIDlist:
        duplicate_list.append(line_split[3])
    else:
        ProductIDlist.append(line_split[3])


f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')

id_json_list = []

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    if line_split[1] in duplicate_list:
        if (line_split[1], line_split[2]) not in id_json_list:
            id_json_list.append((line_split[1], line_split[2]))

    if line_split[3] in duplicate_list:
        if (line_split[3], line_split[4]) not in id_json_list:
            id_json_list.append((line_split[3], line_split[4]))

appear_list = []

for item in id_json_list:
    if item[0] in appear_list:
        print item[0]
    else:
        appear_list.append(item[0])
