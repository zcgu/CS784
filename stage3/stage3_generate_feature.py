import stage3_helper
from stage2 import step4_helper
from py_stringmatching import simfunctions, tokenizers


product_type = 'Product Type'
product_name = 'Product Name'
product_segment = 'Product Segment'
product_long_description = 'Product Long Description'
product_brand = 'Brand'


dictionary = step4_helper.read_dictionary()
dictionary_set = step4_helper.build_dictionary_set(dictionary)


def get_predict_brand(name):
    possible_brands = step4_helper.find_possible_brands(name, dictionary_set, dictionary)
    possible_brands = step4_helper.reduce_possible_brands(name, possible_brands)

    if len(possible_brands) > 0:
        predict_brand = step4_helper.select_from_possible_brands(name, dictionary, possible_brands)
    else:
        predict_brand = step4_helper.find_brand_not_in_dictionary(name)

    if predict_brand is None or predict_brand == '':
        return None
    else:
        return predict_brand


def generate_feature(file_name):
    lines = stage3_helper.read_file(file_name)

    features = []
    labels = []

    for line in lines:
        json1, json2, label = stage3_helper.read_jsons_label_from_line(line)

        feature = []

        # TODO: Add more features and optimize features.

        # product_type
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

        # product_name
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

        # product_segment
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

        # product_long_description
        string1, string2 = stage3_helper.get_attribute_from_jsons(json1, json2, product_long_description)
        if string1 is None or string2 is None:
            feature.append(0.0)
        else:
            feature.append(simfunctions.jaccard(tokenizers.whitespace(string1), tokenizers.whitespace(string2)))

        # product_brand
        string1, string2 = stage3_helper.get_attribute_from_jsons(json1, json2, product_brand)
        string1_name, string2_name = stage3_helper.get_attribute_from_jsons(json1, json2, product_name)

        if string1 is None or string1 == '':
            string1 = get_predict_brand(string1_name)

        if string2 is None or string2 == '':
            string2 = get_predict_brand(string2_name)

        if string1 is None or string2 is None:
            feature.append(0.0)
        else:
            feature.append(simfunctions.jaccard(tokenizers.whitespace(string1), tokenizers.whitespace(string2)))

        # Add one feature and label
        features.append(feature)
        labels.append(stage3_helper.get_01_from_label(label))

    return features, labels
