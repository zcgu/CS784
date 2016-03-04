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

# Read dictionary.
dictionary = read_dictionary()

# Read data into memory.
test_data = read_data(training_set_file_name)         # Need change.

# Main part.
predict_result = []
