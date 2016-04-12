import stage3_helper
import json

product_type = 'Product Type'
product_name = 'Product Name'
product_segment = 'Product Segment'
product_long_description = 'Product Long Description'
product_brand = 'Brand'


def print_wrong_data(file_name, wrong_index):
    lines = stage3_helper.read_file(file_name)
    print len(wrong_index)

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


def contains_similar_model(string1, string2):
    model_strs1 = stage3_helper.find_model_str(string1)
    model_strs2 = stage3_helper.find_model_str(string2)
    for model in model_strs1:
        if model in model_strs2:
            return True
    return False


def hand_code_rule(line):
    json1, json2, label = stage3_helper.read_jsons_label_from_line(line)
    # string1, string2 = stage3_helper.get_attribute_from_jsons(json1, json2, product_name)
    # if contains_similar_model(string1, string2):
    #     return 1

    # string1, string2 = stage3_helper.get_attribute_from_jsons(json1, json2, product_brand)
    # if string1 is not None and string2 is not None and string1 != string2:
    #     return 0

    # string1, string2 = stage3_helper.get_attribute_from_jsons(json1, json2, product_name)
    # if string1 == string2:
    #     return 1

    # string1, string2 = stage3_helper.get_attribute_from_jsons(json1, json2, product_type)
    # if string1.lower() != string2.lower():
    #     return 0
    return None
