import stage3_helper
from py_stringmatching import simfunctions, tokenizers

def generate_feature():
    lines = stage3_helper.read_file('X.txt')

    for line in lines:
        stage3_helper.read_json_label_from_line(line)

    print len(lines)

generate_feature()
