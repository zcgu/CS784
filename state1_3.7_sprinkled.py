
import json
import codecs
import re

ProductName = u'Product Name'
Brand = u'Brand'
Color = u'Color'
Category = u'Category'
ProductType = u'Product Type'


f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')
# map with attribute value, count pair

ProductNameSet = set()
CategorySet = set()
ProductTypeSet = set()
BrandSet = set()

protentialBrandResultMap = {}
protentialProductTypeResultMap = {}
protentialCategoryResultMap = {}

missingBrandProductSet = set()

for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')
    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2


    if Brand not in json1:
        missingBrandProductSet.add(json1.get(ProductName)[0])

    for attribute in json1:
        if attribute == Brand:
            currentBrandName = json1.get(attribute)[0]
            BrandSet.add(currentBrandName)

        if attribute == Category:
            currentCategoryName = json1.get(attribute)[0]
            CategorySet.add(currentCategoryName)

        if attribute == ProductType:
            currentProductType = json1.get(attribute)[0]
            ProductTypeSet.add(currentProductType)

        if attribute == ProductName:
            currentProductName = json1.get(attribute)[0]
            ProductNameSet.add(currentProductName)



for eachProductName in missingBrandProductSet:
    for eachWord in eachProductName.split():
        if eachWord in BrandSet:
            protentialBrandResultMap[eachProductName] = eachWord



print BrandSet
