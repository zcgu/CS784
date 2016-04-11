import stage3_helper
import json


def print_wrong_data(file_name, wrong_index):
    lines = stage3_helper.read_file(file_name)
    fw = open("Wrong_samples.txt", 'w')

    for i in wrong_index:
        json1, json2, label = stage3_helper.read_jsons_label_from_line(lines[i])
        # print json1
        # print json2
        # print 'Label:', label
        # print

        fw.write(json.dumps(json1))
        fw.write('\n')
        fw.write(json.dumps(json2))
        fw.write('\n')
        fw.write('Label:' + label)
        fw.write('\n')
        fw.write('\n')
    fw.close()
