import stage3_helper
from py_stringmatching import simfunctions, tokenizers


product_type = 'Product Type'
product_name = 'Product Name'
product_segment = 'Product Segment'


def generate_feature(file_name):
    lines = stage3_helper.read_file(file_name)

    features = []
    labels = []

    for line in lines:
        json1, json2, label = stage3_helper.read_jsons_label_from_line(line)

        feature = []

        # TODO: Add more features and optimize features.
        string1, string2 = stage3_helper.get_attribute_from_jsons(json1, json2, product_type)
        feature.append(simfunctions.jaccard(tokenizers.qgram(string1, 3), tokenizers.qgram(string2, 3)))
        feature.append(simfunctions.jaro_winkler(string1, string2, prefix_weight=0.1))
        if(len(string1) == len(string2)):
            feature.append(simfunctions.hamming_distance(string1, string2))
        else:
            feature.append(5)
        feature.append(simfunctions.cosine(stage3_helper.stringToSet(string1),stage3_helper.stringToSet(string2)))
        feature.append(simfunctions.overlap_coefficient(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))
        feature.append(simfunctions.monge_elkan(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))
        feature.append(simfunctions.tfidf(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))

        string1, string2 = stage3_helper.get_attribute_from_jsons(json1, json2, product_name)
        feature.append(simfunctions.jaccard(tokenizers.qgram(string1, 3), tokenizers.qgram(string2, 3)))
        feature.append(simfunctions.jaro_winkler(string1, string2, prefix_weight=0.1))
        if(len(string1) == len(string2)):
            feature.append(simfunctions.hamming_distance(string1, string2))
        else:
            feature.append(5)
        feature.append(simfunctions.cosine(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))
        feature.append(simfunctions.overlap_coefficient(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))
        feature.append(simfunctions.monge_elkan(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))
        feature.append(simfunctions.tfidf(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))

        string1, string2 = stage3_helper.get_attribute_from_jsons(json1, json2, product_segment)
        feature.append(simfunctions.jaccard(tokenizers.qgram(string1, 3), tokenizers.qgram(string2, 3)))
        feature.append(simfunctions.jaro_winkler(string1, string2, prefix_weight=0.1))
        if(len(string1) == len(string2)):
            feature.append(simfunctions.hamming_distance(string1, string2))
        else:
            feature.append(5)
        feature.append(simfunctions.cosine(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))
        feature.append(simfunctions.overlap_coefficient(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))
        feature.append(simfunctions.monge_elkan(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))
        feature.append(simfunctions.tfidf(stage3_helper.stringToSet(string1), stage3_helper.stringToSet(string2)))

        features.append(feature)
        labels.append(stage3_helper.get_01_from_label(label))

    return features, labels
