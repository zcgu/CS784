import codecs
import json
from py_stringmatching import simfunctions, tokenizers
import re



def read_file(file_name):
    f = codecs.open(file_name, 'r', errors='ignore')

    raw_lines = f.read().splitlines()
    lines = []

    for line in raw_lines:
        lines.append(unicode(line, errors='ignore'))

    return lines


def read_jsons_label_from_line(line):
    line_split = line.split('?')

    json1 = json.loads(line_split[2])   # json for product 1
    json2 = json.loads(line_split[4])   # json for product 2

    if len(line_split) < 6:
        label = None
    else:
        label = line_split[5]

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
        return 1
    elif label == 'MISMATCH':
        return 0
    else:
        return None


def get_label_from_01(b):
    if b == 1:
        return 'MATCH'
    elif b == 0:
        return 'MISMATCH'
    else:
        print 'Error get_01_from_label'
        return None


def accuracy(labels, predict_labels):
    if len(labels) != len(predict_labels):
        print 'Error accuracy()'
        return None

    total_positive = 0.
    true_positive = 0.
    false_positive = 0.
    for i in range(0, len(labels)):
        if labels[i] == 1:
            total_positive += 1
        if predict_labels[i] == 1 and predict_labels[i] == labels[i]:
            true_positive += 1
        if predict_labels[i] == 1 and predict_labels[i] != labels[i]:
            false_positive += 1

    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / total_positive
    return precision, recall


def find_model_str(name, min_len=5):
    model_strs = []
    for string in tokenizers.whitespace(name):
        if len(string) < min_len:
            continue
        contains_symbol = False
        for char in string:
            if not char.isalpha():
                contains_symbol = True
        if contains_symbol:
            model_strs.append(string)
    return model_strs


TAG_RE = re.compile(r'<[^>]+>')


def cleanhtml(text):
    return TAG_RE.sub('', text)


cachedStopWords = read_file("stopwords.txt")


def clean_stop_word(string):
    return ' '.join([word for word in string.split() if word not in cachedStopWords])


def output_threshold_for_low_prob(predict_labels, predict_prob, threshold):
    for i in range(0, len(predict_labels)):
        if predict_prob[i][0] > threshold:
            predict_labels[i] = 0
        else:
            predict_labels[i] = 1
    return predict_labels
