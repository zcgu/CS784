import json
import codecs

f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')

long_description = 'Product Long Description'
short_description = 'Product Short Description'

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2

    if long_description in json1 and short_description in json1:
        if len(json1[long_description][0]) < len(json1[short_description][0]):
            print line_split[1]
            print json1[long_description][0]
            print json1[short_description][0]
            print

    if long_description in json2 and short_description in json2:
        if len(json2[long_description][0]) < len(json2[short_description][0]):
            print line_split[3]
            print json2[long_description][0]
            print json2[short_description][0]
            print