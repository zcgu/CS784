import json
import codecs
import re



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
        matchWordCount = 0
        for innerKey, innerValue in productTypeMapWordList.iteritems():
            if innerKey == key:
                continue
            else:
                outValueList = []
                for word in value:
                    word = re.sub('[^0-9a-zA-Z]+', '', word.lower())
                    outValueList.append(word)
                innerValueList = []
                for word in innerValue:
                    word = re.sub('[^0-9a-zA-Z]+', '', word.lower())
                    innerValueList.append(word)

                outValueLen = len(outValueList)
                innerValueLen = len(innerValueList)
                matchNum = 0
                if(outValueLen < innerValueList):
                    for eachValue in outValueList:
                        if eachValue in innerValueList:
                            matchNum = matchNum + 1
                        else:
                            if eachValue:
                                if eachValue[-1] == 's':
                                    if eachValue[:-1] == innerValueList[-1]:
                                        matchNum = matchNum + 1


                else:
                    for eachValue in innerValueList:
                        if eachValue in outValueList:
                            matchNum = matchNum + 1
                        else:
                            if eachValue:
                                if eachValue[-1] == 's':
                                    if eachValue[:-1] == outValueList[-1]:
                                        matchNum = matchNum + 1
                if matchNum >=2:
                    tempSet.add(key)
                    tempSet.add(innerKey)


        if(tempSet):
            allList.insert(index, tempSet)
            index = index + 1
print allList

for a in allList:
    print a