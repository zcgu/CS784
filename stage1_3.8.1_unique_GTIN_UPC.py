import json
import codecs

f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')

id_GTIN_list = []
attribute = u'UPC'
# attribute = u'GTIN'

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2

    if attribute in json1:
        if (line_split[1], json1[attribute]) not in id_GTIN_list:
            id_GTIN_list.append((line_split[1], json1[attribute]))

    if attribute in json2:
        if (line_split[3], json2[attribute]) not in id_GTIN_list:
            id_GTIN_list.append((line_split[3], json2[attribute]))

duplicate_id_list = []

for item in id_GTIN_list:
    if item[0] in duplicate_id_list:
        print item[0]
    else:
        duplicate_id_list.append(item[0])
