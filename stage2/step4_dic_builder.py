import codecs
import json
import enchant

dictionary_file_name = 'elec_brand_dic.txt'
dictionary_out_name = 'step4_dictionary'

common_dictionary = enchant.Dict("en_GB")


common_suffix = ['inc', 'inc.', 'technology', 'technologies', 'tech', 'international',
                 'electronic', 'electronics', 'electric']


def read_dictionary():
    """
    Read the original dictionary given by professor.
    Delete '\n' and space at the end.

    :return: A dictionary in array.
    """

    dictionary = []
    f = codecs.open(dictionary_file_name, 'r', errors='ignore')
    for line in f:
        line = unicode(line, errors='ignore')

        while line[len(line) - 1] == '\n':
            line = line[:len(line) - 1]

        while line[len(line) - 1].isdigit():
            line = line[:len(line) - 1]

        while line[len(line) - 1].isspace():
            line = line[:len(line) - 1]

        if len(line) == 0:
            print 'error'

        dictionary.append(line)

    print 'Finish reading dictionary.'

    return dictionary


def convert_dictionary_to_lower(dictionary):
    """
    Convert all of the character in dictionary to lower case.

    :param dictionary: The dictionary.
    :return: Dictionary after convert.
    """

    lower_dictionary = []
    for brand in dictionary:
        lower_dictionary.append(brand.lower())
    return lower_dictionary


def increase_dictionary(dictionary):
    """
    Add some common suffix to all of the brand in dictionary.
    e.g., Add 'rockland inc', 'rockland inc.', 'rockland technology', etc. for 'rockland'.
    Add 'rockland' for 'rockland technology'.
    And won't add common words as a brand.
    e.g., do not add 'cable' for 'cable technology'.

    :param dictionary: The dictionary in array.
    :return: Dictionary after add words.
    """

    i = 0
    while i < len(dictionary):
        brand = dictionary[i]

        last_space_pos = brand.rfind(' ')
        if last_space_pos == -1:
            last_word = brand
            previous_word = brand
        else:
            last_word = brand[last_space_pos + 1:]
            previous_word = brand[:last_space_pos]

        if last_word in common_suffix:
            prefix = previous_word
        else:
            prefix = brand

        for single_suffix in common_suffix:
            if prefix + ' ' + single_suffix not in dictionary:
                dictionary.insert(i, prefix + ' ' + single_suffix)
                i += 1

        if prefix not in dictionary and not common_dictionary.check(prefix):
            dictionary.insert(i, prefix)
            i += 1

        i += 1

    return dictionary


#########################################################################################

dictionary = read_dictionary()
dictionary = convert_dictionary_to_lower(dictionary)
dictionary = increase_dictionary(dictionary)

fw = codecs.open(dictionary_out_name, 'w')

for brand in dictionary:
    fw.write(brand)
    fw.write('\n')

fw.close()
