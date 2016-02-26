import json
import codecs
import re

f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')

attribute_list = [u'Product Type', u'Product Name', u'Product Segment',
                  u'Product Long Description', u'Brand',u'Product Short Description',
                  u'GTIN', u'UPC', u'Country of Origin: Components', u'Category']

attribute = attribute_list[5]

list = []


def suspect(string):
    string_symbol = re.sub('[0-9a-zA-Z]+', '', string)

    if len(string_symbol) > 1.0 * len(string) / 2:
        return True
    else:
        return False

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2

    if attribute in json1:
        if suspect(json1[attribute][0]):
            print line_split[1]
            print json1[attribute][0]
            print
            list.append((line_split[1], attribute, json1[attribute][0]))

    if attribute in json2:
        if suspect(json2[attribute][0]):
            print line_split[3]
            print json2[attribute][0]
            print
            list.append((line_split[3], attribute, json2[attribute][0]))

print list
