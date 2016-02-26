import json
import codecs

f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')

attribute_map = {}

id_list = []

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2

    # print json1
    # store the attribute type and occurrence times
    if line_split[1] not in id_list:
        id_list.append(line_split[1])
        for attribute in json1:
            # print attribute
            if attribute in attribute_map:
                attribute_map[attribute] += 1
            else:
                attribute_map[attribute] = 1

    if line_split[3] not in id_list:
        id_list.append(line_split[3])
        for attribute in json2:
            # print attribute
            if attribute in attribute_map:
                attribute_map[attribute] += 1
            else:
                attribute_map[attribute] = 1

# sort attribute
sorted_list = sorted(attribute_map.items(), key=lambda d: d[1], reverse=True)
print sorted_list

f = open("stage1_2_output", 'w')
f.write(str(sorted_list))
