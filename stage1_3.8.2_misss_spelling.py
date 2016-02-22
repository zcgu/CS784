import enchant
import json
import codecs
import re

f = codecs.open('elec_pairs_stage1.txt', 'r', errors='ignore')

attribute_list = [u'Product Type', u'Product Name', u'Product Segment',
                  u'Product Long Description', u'Brand', u'Product Short Description',
                  u'GTIN', u'UPC', u'Country of Origin: Components', u'Category']

attribute = attribute_list[5]

my_dic = ['li', 'ul', 'iPad', 'eNet']


def suspect(string):
    d = enchant.Dict("en_US")
    if d.check(string):
        return False

    if string in my_dic:
        return False

    return True


for line in f:
    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2

    if attribute in json1:
        word_split = re.split('[^a-zA-Z]+', json1[attribute][0])
        for word in word_split:
            if len(word) == 0:
                continue

            if word[0] != word[0].lower():
                continue

            if suspect(word):
                print word
                print json1[attribute][0]
                print


