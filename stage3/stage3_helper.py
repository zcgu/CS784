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


def read_json_label_from_line(line):
    line_split = line.split('?')

    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2

    label = line_split[5]

    if label != 'MATCH' and label != 'MISMATCH':
        print 'Error read_json_label_from_line'

    return json1, json2, label
