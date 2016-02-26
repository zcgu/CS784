# Step 2. From the set of 10K labeled product pairs, randomly sample 350 products.
# Let this sample be S. For each product in S,
# go into the attribute "Product Name" and pull out the correct band name (if exists).
# This will give you the golden data (that you can use to debug, estimate accuracy, etc.).


# This script will generate 350 samples with product name.


import json
import codecs
import random

# First, find the total number of products.

f = codecs.open('elec_pairs_stage2.txt', 'r', errors='ignore')

product_id_list = []

for line in f:

    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    if len(line_split[2]) > 0:
        json1 = json.loads(line_split[2])   # json for product 1
    if len(line_split[4]) > 0:
        json2 = json.loads(line_split[4])   # json for product 2

    if line_split[1] not in product_id_list:
        product_id_list.append(line_split[1])

    if line_split[3] not in product_id_list:
        product_id_list.append(line_split[3])

print "Total number of products is: " + str(len(product_id_list))

# Total number of products is: 18461

# Next, generate random 350 index.

sample_index_list = []

for i in range(1, len(product_id_list)+1):
    sample_index_list.append(i)

random.seed(1234567)

sample_index_list = random.sample(sample_index_list, 350)

print sample_index_list

# Finally, pull out those 350 samples.

f = codecs.open('elec_pairs_stage2.txt', 'r', errors='ignore')
fw = open("step2_samples.txt", 'w')

product_id_list = []

PRODUCT_NAME = u'Product Name'
BRAND = u'Brand'
PRODUCT_ID = u'Product ID'

for line in f:

    line = unicode(line, errors='ignore')
    line_split = line.split('?')

    name1 = ''
    if len(line_split[2]) > 0:
        json1 = json.loads(line_split[2])   # json for product 1
        if PRODUCT_NAME in json1:
            name1 = json1[PRODUCT_NAME][0]

    name2 = ''
    if len(line_split[4]) > 0:
        json2 = json.loads(line_split[4])   # json for product 2
        if PRODUCT_NAME in json2:
            name2 = json2[PRODUCT_NAME][0]

    if line_split[1] not in product_id_list:
        product_id_list.append(line_split[1])
        if len(product_id_list) in sample_index_list:
            data = {BRAND: '', PRODUCT_NAME: name1, PRODUCT_ID: line_split[1]}
            json_data = json.dumps(data)
            fw.write(json_data)
            if len(product_id_list) != max(sample_index_list):
                fw.write('\n')

    if line_split[3] not in product_id_list:
        product_id_list.append(line_split[3])
        if len(product_id_list) in sample_index_list:
            data = {BRAND: '', PRODUCT_NAME: name2, PRODUCT_ID: line_split[3]}
            json_data = json.dumps(data)
            fw.write(json_data)
            if len(product_id_list) != max(sample_index_list):
                fw.write('\n')

fw.close()
