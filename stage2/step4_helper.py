import codecs
import json

dictionary_file_name = 'elec_brand_dic.txt'


def read_dictionary():
    dictionary = []
    f = codecs.open(dictionary_file_name, 'r', errors='ignore')
    for line in f:
        line = unicode(line, errors='ignore')
        line_split = line.split()
        if len(line_split[0]) == 0:
            print 'error'
        dictionary.append(line_split[0])

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
