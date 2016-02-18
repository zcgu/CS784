import json
import codecs




Category = u'Category'
ProductType = u'Product Type'


f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')
# map with attribute value, count pair
categoryMapCount = {}
productTypeMapCount = {}

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')
    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2
    for attribute in json1:
        if attribute == Category:
            currentAttributeValue = json1.get(attribute)[0]
            if currentAttributeValue in categoryMapCount:
                categoryMapCount[currentAttributeValue] += 1
            else:
                categoryMapCount[currentAttributeValue] = 1
        if attribute == ProductType:
            currentAttributeValue = json1.get(attribute)[0]
            if currentAttributeValue in productTypeMapCount:
                productTypeMapCount[currentAttributeValue] += 1
            else:
                productTypeMapCount[currentAttributeValue] = 1


# try to see the suspect related members
categoryMapWordList = {}
productTypeMapWordList = {}
for key in productTypeMapCount:
    keyWordList = key.split()
    productTypeMapWordList[key] = keyWordList

for key in categoryMapCount:
    keyWordList = key.split()
    categoryMapWordList[key] = keyWordList

allList = []
index = 0
for key, value in productTypeMapWordList.iteritems():
        tempSet = set()
        for eachWord in value:
            for innerKey, innerValue in productTypeMapWordList.iteritems():
                if innerKey == key:
                    continue
                else:
                    if eachWord in innerValue:
                        tempSet.add(key)
                        tempSet.add(innerKey)
        if(tempSet):
            allList.insert(index, tempSet)
            index = index + 1
print allList
