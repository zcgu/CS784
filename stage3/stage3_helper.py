import codecs
import json

def read_file(file_name):
    f = codecs.open(file_name, 'r', errors='ignore')

    # lines = []
    #
    # for line in f:
    #     line = unicode(line, errors='ignore')
    #     lines.append(line)

    raw_lines = f.read().splitlines()
    lines = []

    for line in raw_lines:
        lines.append(unicode(line, errors='ignore'))

    return lines


def read_jsons_label_from_line(line):
    line_split = line.split('?')

    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2

    label = line_split[5]

    if label != 'MATCH' and label != 'MISMATCH':
        print 'Error read_json_label_from_line'

    return json1, json2, label


def get_attribute_from_jsons(json1, json2, attribute):
    if attribute in json1:
        string1 = json1[attribute][0]
    else:
        string1 = None

    if attribute in json2:
        string2 = json2[attribute][0]
    else:
        string2 = None

    return string1, string2


def get_01_from_label(label):
    if label == 'MATCH':
        return 0
    elif label == 'MISMATCH':
        return 1
    else:
        print 'Error get_01_from_label'
        return None


def get_label_from_01(b):
    if b == 0:
        return 'MATCH'
    elif b == 1:
        return 'MISMATCH'
    else:
        print 'Error get_01_from_label'
        return None
