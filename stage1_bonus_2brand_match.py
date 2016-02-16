import json
import codecs
import re

# Top 10:
# [u'Product Type', u'Product Name', u'Product Segment', u'Product Long Description', u'Brand',
#  u'Product Short Description', u'GTIN', u'UPC', u'Country of Origin: Components', u'Category']

brand = u'Brand'
name = u'Product Name'
same_brand = [('HP', 'Hewlett Packard'), ('GN Netcom', 'Jabra'), ('EP Memory', 'J5 Create'),
              ('Eveready', 'Energizer'), ('BIC VENTURI', 'BIC America'), ('Directed Electronics', 'DEI'),
              ('American Power Conversion', 'APC')]


def suspect(json1, json2):
    brand1_raw = json1[brand][0]
    brand1 = re.sub('[^0-9a-zA-Z]+', '', brand1_raw.lower())

    brand2_raw = json2[brand][0]
    brand2 = re.sub('[^0-9a-zA-Z]+', '', brand2_raw.lower())

    name1 = json1[name][0].lower()

    name2 = json2[name][0].lower()

    if brand1 in brand2 or brand2 in brand1:
        return False

    for word in brand1_raw.lower().split():
        if word in brand2_raw.lower():
            return False

    for word in brand2_raw.lower().split():
        if word in brand1_raw.lower():
            return False

    if (brand1_raw, brand2_raw) in same_brand:
        return False

    if (brand2_raw, brand1_raw) in same_brand:
        return False

    if brand1_raw.lower() in name2:
        return False

    if brand2_raw.lower() in name1:
        return False

    return True


f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2
    is_match = line_split[5]

    if brand in json1 and brand in json2 and is_match == 'MATCH\n':

        if suspect(json1, json2):
            print json1[brand][0] + ", " + json2[brand][0]
            print json1[name][0]
            print json2[name][0]
            print line

