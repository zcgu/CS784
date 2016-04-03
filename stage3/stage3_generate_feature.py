import stage3_helper
from py_stringmatching import simfunctions, tokenizers


def generate_feature():
    lines = stage3_helper.read_file('X_training.txt')

    json_label_list = []
    for line in lines:
        json1, json2, label = stage3_helper.read_json_label_from_line(line)
        json_label_list.append((json1, json2, label))

    features = []
    labels = []

generate_feature()
