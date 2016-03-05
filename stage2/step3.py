# Step 3. Randomly split S into a development set I and a testing set J.
# The set I must have at least 200 products and the set J must have at least 120 products.

import json
import codecs
import random

golden_data_file_name = 'step2_golden_data.txt'
training_set_file_name = 'step2_training_set'
tuning_set_file_name = 'step2_tuning_set'
testing_set_file_name = 'step2_testing_set'

product_brand = 'Brand'

training_data_size = 160
tuning_data_size = 60
testing_data_size = 130

f = codecs.open(golden_data_file_name, 'r', errors='ignore')
golden_data = []

for line in f:

    line = unicode(line, errors='ignore')

    record_json = json.loads(line)

    if len(record_json[product_brand]) > 0:
        while record_json[product_brand][len(record_json[product_brand]) - 1].isspace():
            record_json[product_brand] = record_json[product_brand][:len(record_json[product_brand]) - 1]

    golden_data.append(record_json)


print len(golden_data)

# DO NOT change this seed.
random.seed(893435071)
random.shuffle(golden_data)

fw = open(training_set_file_name, 'w')
for i in range(0, training_data_size):
    fw.write(json.dumps(golden_data[i]))
    fw.write('\n')
fw.close()

fw = open(tuning_set_file_name, 'w')
for i in range(training_data_size, training_data_size + tuning_data_size):
    fw.write(json.dumps(golden_data[i]))
    fw.write('\n')
fw.close()

fw = open(testing_set_file_name, 'w')
for i in range(training_data_size + tuning_data_size, training_data_size + tuning_data_size + testing_data_size):
    fw.write(json.dumps(golden_data[i]))
    fw.write('\n')
fw.close()

