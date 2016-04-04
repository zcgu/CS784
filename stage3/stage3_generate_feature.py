import stage3_helper
from py_stringmatching import simfunctions, tokenizers


product_type = 'Product Type'
product_name = 'Product Name'
product_segment = 'Product Segment'


def generate_feature():
    lines = stage3_helper.read_file('X_training.txt')

    jsons_label_list = []
    for line in lines:
        json1, json2, label = stage3_helper.read_jsons_label_from_line(line)
        jsons_label_list.append((json1, json2, label))

    features = []
    labels = []
    for jsons_label in jsons_label_list:
        feature = []

        string1, string2 = stage3_helper.get_attribute_from_jsons(jsons_label[0], jsons_label[1], product_type)
        feature.append(simfunctions.jaccard(tokenizers.qgram(string1, 3), tokenizers.qgram(string2, 3)))

        string1, string2 = stage3_helper.get_attribute_from_jsons(jsons_label[0], jsons_label[1], product_name)
        feature.append(simfunctions.jaccard(tokenizers.qgram(string1, 3), tokenizers.qgram(string2, 3)))

        string1, string2 = stage3_helper.get_attribute_from_jsons(jsons_label[0], jsons_label[1], product_segment)
        feature.append(simfunctions.jaccard(tokenizers.qgram(string1, 3), tokenizers.qgram(string2, 3)))

        features.append(feature)
        labels.append(stage3_helper.get_01_from_label(jsons_label[2]))

    return features, labels

generate_feature()
