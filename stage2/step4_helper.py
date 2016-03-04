import codecs
import json

dictionary_file_name = 'elec_brand_dic.txt'


def read_dictionary():
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


def read_data(file_name):
    data = []
    f = codecs.open(file_name, 'r', errors='ignore')
    for line in f:
        line = unicode(line, errors='ignore')
        record_json = json.loads(line)
        data.append(record_json)

    print 'Finish reading data.'

    return data


def convert_dictionary_to_lower(dictionary):
    lower_dictionary = []
    for brand in dictionary:
        lower_dictionary.append(brand.lower())
    return lower_dictionary


def find_possible_brands(item_name, dictionary):

    lower_dictionary = convert_dictionary_to_lower(dictionary)

    possible_brands = []

    item_name_split = item_name.split()

    for length in range(1, 5):
        for position in range(0, len(item_name_split) - length):
            string = item_name_split[position]

            for i in range(1, length):
                string += ' '
                string += item_name_split[position + i]

            if string.lower() in lower_dictionary:
                possible_brands.append(string)

    possible_brands = sorted(possible_brands, key=lambda b: lower_dictionary.index(b.lower()), reverse=False)

    for name in possible_brands:
        for other_name in possible_brands:
            if other_name != name and name in other_name:
                possible_brands.remove(name)

    # print possible_brands

    return possible_brands
