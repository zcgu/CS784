# Step 4. Now use the development set I to develop your brand name extractor.
# You can use any method youd like.
# If you decide to use the dictionary based approach, we have supplied a dictionary of brand names for you.
# YOU CAN ONLY USE THE DEVELOPMENT SET I. YOU ARE NOT SUPPOSED TO EVEN LOOK AT THE TESTING SET J.
# We will discuss more in the class ideas on using the development set I.

import codecs
from step4_helper import *

# File names.
golden_data_file_name = 'step2_golden_data.txt'

training_set_file_name = 'step2_training_set'
tuning_set_file_name = 'step2_tuning_set'
testing_set_file_name = 'step2_testing_set'

product_id = 'Product ID'
product_name = 'Product Name'
product_brand = 'Brand'

# Read dictionary.
dictionary = read_dictionary()

# Read data into memory.
test_data = read_data(training_set_file_name)

# Main part.
predict_result = []

total_positive = 0.0
true_positive = 0.0
false_positive = 0.0

for item in test_data:
    item_id = item[product_id]
    item_name = item[product_name]
    item_brand = item[product_brand]

    # print 'item_name: ' + item_name
    # print 'item_brand: ' + item_brand
    possible_brands = find_possible_brands(item_name, dictionary)

    if len(possible_brands) > 0:
        predict_brand = possible_brands[0]
        # print "predict_brand: " + predict_brand
    else:
        predict_brand = ''
        # print "predict_brand: Not Found!"

    if item_brand != '':
        total_positive += 1
    if predict_brand != '' and predict_brand == item_brand:
        true_positive += 1
    if predict_brand != '' and predict_brand != item_brand:
        false_positive += 1

    if item_brand != '' and predict_brand != item_brand:
        print 'item_name: ' + item_name
        print 'item_brand: ' + item_brand
        print 'possible_brands: ' + str(possible_brands)
        print 'predict_brand: ' + predict_brand
        print
    # print

print

print 'total_positive: ' + str(total_positive)
print 'true_positive: ' + str(true_positive)
print 'false_positive: ' + str(false_positive)

print 'precision: ' + str(true_positive / (true_positive + false_positive))
print 'recall: ' + str(true_positive / total_positive)
