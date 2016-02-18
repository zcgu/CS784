import json
import codecs




Category = u'Category'
ProductType = u'Product Type'


f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')
categoryMap = {}
productTypeMap = {}


for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')
    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2
    for attribute in json1:
        if attribute == Category:
            currentAttributeValue = json1.get(attribute)[0]
            if currentAttributeValue in categoryMap:
                categoryMap[currentAttributeValue] += 1
            else:
                categoryMap[currentAttributeValue] = 1
        if attribute == ProductType:
            currentAttributeValue = json1.get(attribute)[0]
            if currentAttributeValue in productTypeMap:
                productTypeMap[currentAttributeValue] += 1
            else:
                productTypeMap[currentAttributeValue] = 1

print productTypeMap
print categoryMap
print "x"

