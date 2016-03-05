import codecs
import json
import re
import enchant

dictionary_out_name = 'step4_dictionary'

common_suffix = ['inc', 'inc.', 'technology', 'technologies', 'tech', 'international',
                 'electronic', 'electronics', 'electric']

def read_dictionary():
    dictionary = []
    f = codecs.open(dictionary_out_name, 'r', errors='ignore')
    for line in f:
        line = unicode(line, errors='ignore')

        while line[len(line) - 1] == '\n':
            line = line[:len(line) - 1]

        dictionary.append(line)

    print 'Finish reading dictionary.'

    return dictionary


def build_dictionary_set(dictionary):
    dictionary_set = set()
    for brand in dictionary:
        dictionary_set.add(brand)
    return dictionary_set


def read_data(file_name):
    data = []
    f = codecs.open(file_name, 'r', errors='ignore')
    for line in f:
        line = unicode(line, errors='ignore')
        record_json = json.loads(line)
        data.append(record_json)

    print 'Finish reading data.'

    return data


def find_possible_brands(item_name, dictionary_set, dictionary):

    possible_brands = []

    item_name_split = item_name.split()

    # Find every words between length 1 and 5.
    # See if they in dictionary.
    for length in range(1, 5):
        for position in range(0, len(item_name_split) - length):
            string = item_name_split[position]

            for i in range(1, length):
                string += ' '
                string += item_name_split[position + i]

            while len(string) != 0 and not string[0].isdigit() and not string[0].isalpha():
                string = string[1:]
            while len(string) != 0 and not string[len(string) - 1].isdigit() and not string[len(string) - 1].isalpha():
                string = string[:len(string) - 1]

            if string.lower() in dictionary_set:
                possible_brands.append(string)
            elif re.sub('[^0-9a-zA-Z]+', '', string.lower()) in dictionary_set:
                dictionary_set.add(string.lower())
                dictionary.insert(dictionary.index(re.sub('[^0-9a-zA-Z]+', '', string.lower())), string.lower())
                possible_brands.append(string)
            elif re.sub('[^0-9a-zA-Z]+', ' ', string.lower()) in dictionary_set:
                dictionary_set.add(string.lower())
                dictionary.insert(dictionary.index(re.sub('[^0-9a-zA-Z]+', ' ', string.lower())), string.lower())
                possible_brands.append(string)

    return possible_brands


def reduce_possible_brands(item_name, possible_brands):

    # If we found 'Tripp', 'Lite' and 'Tripp Lite' for for 'Tripp Lite Standard Power Cord ...'.
    # Remove 'Tripp' and 'Lite', Keep 'Tripp Lite'.

    new_possible_brands = possible_brands[:]
    for name in possible_brands:
        for other_name in possible_brands:
            if other_name != name and name in other_name:
                index = other_name.find(name)
                if index > 0:
                    if other_name[index - 1] != ' ':
                        continue
                if index + len(name) < len(other_name):
                    if other_name[index + len(name)] != ' ':
                        continue

                new_possible_brands.remove(name)
                break
    possible_brands = new_possible_brands[:]

    for name in possible_brands:
        index = item_name.find(name)
        if index <= 0:
            continue

        prefix = item_name[:index - 1]
        space_index = prefix.rfind(' ')
        if space_index == -1:
            continue

        previous_word = prefix[space_index + 1:]

        if previous_word.lower() == 'for':
            possible_brands.remove(name)

    return possible_brands


def select_from_possible_brands(item_name, dictionary, possible_brands):

    # If any brand is at the beginning of the name, they choose it as brand.
    # Otherwise choose the most common brand
    for brand_name in possible_brands:
        if item_name.find(brand_name) == 0:
            return brand_name

    for brand_name in possible_brands:
        if item_name.find(brand_name) == item_name.find(' ') + 1:
            return brand_name

    # Convert dictionary to lower case.
    # Sort the brand names by the frequency (The index in dictionary).
    possible_brands = sorted(possible_brands, key=lambda b: dictionary.index(b.lower()), reverse=False)
    return possible_brands[0]


# See if the first few words
def find_brand_not_in_dictionary(item_name):

    item_name_split = item_name.split()
    common_dictionary = enchant.Dict("en_US")

    # Looking for 'xxx Tech ...'.
    for string in item_name_split:
        if item_name_split.index(string) > 4:
            break
        if item_name_split.index(string) == 0:
            continue
        if string.lower() in common_suffix:
            return item_name[:item_name.find(string) + len(string)]

    # Looking for 'DOLPHIN COMPONENTS CORP DC-8AHM Cabl'.
    for string in item_name_split:
        if item_name_split.index(string) > 4:
            return item_name[:item_name.find(string) - 1]
        if item_name_split.index(string) == 0 and not string_all_upper(string):
            break
        if not string_all_upper(string):
            return item_name[:item_name.find(string) - 1]

    # Looking for 'GoLight 3100 Stryker...'
    if len(item_name_split) >= 2:
        if not common_dictionary.check(item_name_split[0]) \
                and not string_contains_digit(item_name_split[0]) \
                and (string_contains_digit(item_name_split[1]) or common_dictionary.check(item_name_split[1])):
            return item_name_split[0]

    # Looking for 'Print Logic 5xxx ...'
    if len(item_name_split) >= 3:
        if not common_dictionary.check(item_name_split[0]) \
                and not string_contains_digit(item_name_split[0]) \
                and not common_dictionary.check(item_name_split[1]) \
                and not string_contains_digit(item_name_split[1]) \
                and (string_contains_digit(item_name_split[2]) or common_dictionary.check(item_name_split[2])):
            return item_name[:item_name.find(item_name_split[2]) - 1]

    return ''


def string_contains_digit(string):
    for char in string:
        if char.isdigit():
            return True
    return False

def string_all_upper(string):
    for char in string:
        if not char.isupper():
            return False
    return True
