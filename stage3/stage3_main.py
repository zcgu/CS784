import stage3_helper
import stage3_generate_feature
import stage3_hand_code_rule
from sklearn import tree
from sklearn import ensemble
from sklearn import naive_bayes
from sklearn import svm
from sklearn import linear_model
from sklearn.cross_validation import StratifiedKFold
import numpy


features_X, labels_X, data_lines = stage3_generate_feature.generate_feature('X.txt')

skf = StratifiedKFold(labels_X, 5)


def train_model(model):
    labels = []
    predict_labels = []
    predict_prob = []
    wrong_index = []
    for train, test in skf:
        features_train = []
        labels_train = []
        features_test = []
        labels_test = []

        for index in train:
            features_train.append(features_X[index])
            labels_train.append(labels_X[index])
        for index in test:
            features_test.append(features_X[index])
            labels_test.append(labels_X[index])

        clf = model(n_estimators=1000)
        clf = clf.fit(features_train, labels_train)
        predict_labels_test = clf.predict(features_test)
        predict_labels_prob = clf.predict_proba(features_test)

        for i in range(0, len(test)):
            if stage3_hand_code_rule.hand_code_rule(data_lines[test[i]]) is not None:
                predict_labels_test[i] = stage3_hand_code_rule.hand_code_rule(data_lines[test[i]])

        for label in labels_test:
            labels.append(label)
        for label in predict_labels_test:
            predict_labels.append(label)
        for prob in predict_labels_prob:
            predict_prob.append(prob)

        for i in range(0, len(labels_test)):
            if labels_test[i] != predict_labels_test[i]:
                wrong_index.append(test[i])
    return labels, predict_labels, wrong_index, predict_prob


def print_result(model_name, labels, predict_labels):
    print model_name
    print 'Result:' + '(precision, recall)'
    print str(stage3_helper.accuracy(labels, predict_labels))
    print ''


def stage3_predict():
    features_test, labels_test, data_lines_3 = stage3_generate_feature.generate_feature('elec_pairs_stage3_test1.txt')
    # features_test, labels_test, data_lines_3 = stage3_generate_feature.generate_feature('Y.txt')
    clf = ensemble.RandomForestClassifier(n_estimators=1000)
    clf = clf.fit(features_X, labels_X)
    predict_labels_stage3 = clf.predict(features_test)
    predict_prob_stage3 = clf.predict_proba(features_test)
    return labels_test, predict_labels_stage3, predict_prob_stage3, data_lines_3


def stage3_output(data_lines_test, predict_labels_test):
    fw = open("stage3_output.txt", 'w')
    for i in range(0, len(data_lines_test)):
        pair_id = data_lines_test[i].split('?')[0]
        match_mismatch = stage3_helper.get_label_from_01(predict_labels_test[i])
        fw.write(pair_id + ', ' + match_mismatch)
        if i != len(data_lines_test) - 1:
            fw.write('\n')
    fw.close()


# # Decision Tree
# clf = tree.DecisionTreeClassifier()  # TODO: add parameters
# labels, predict_labels, wrong_index = train_model(tree.DecisionTreeClassifier)
# print_result('Decision Tree', labels, predict_labels)
#
# # Random Forest
# labels, predict_labels, wrong_index = train_model(ensemble.RandomForestClassifier)
# print_result('Random Forest', labels, predict_labels)
#
# # Gaussian Naive Bayes
# labels, predict_labels, wrong_index = train_model(naive_bayes.GaussianNB)
# print_result('Gaussian Naive Bayes', labels, predict_labels)
#
# # Multinomial Naive Bayes
# labels, predict_labels, wrong_index = train_model(naive_bayes.MultinomialNB)
# print_result('Multinomial Naive Bayes', labels, predict_labels)
#
# # Bernoulli Naive Bayes
# labels, predict_labels, wrong_index = train_model(naive_bayes.BernoulliNB)
# print_result('Bernoulli Naive Bayes', labels, predict_labels)
#
# # SVM-SVC
# labels, predict_labels, wrong_index = train_model(svm.SVC)
# print_result('SVM-SVC', labels, predict_labels)
#
# # SVM-NuSVC
# labels, predict_labels, wrong_index = train_model(svm.NuSVC)
# print_result('SVM-NuSVC', labels, predict_labels)
#
# # Logistic Regression
# labels, predict_labels, wrong_index = train_model(linear_model.LogisticRegression)
# print_result('Logistic Regression', labels, predict_labels)




# labels, predict_labels, wrong_index, predict_prob = train_model(ensemble.RandomForestClassifier)
# for threshold in numpy.arange(0.4, 0.6, 0.01):
#     print 'Threshold:', threshold
#     predict_labels = stage3_helper.output_threshold_for_low_prob(predict_labels, predict_prob, threshold)
#     print_result('Random Forest', labels, predict_labels)
#
# stage3_hand_code_rule.print_wrong_data('X.txt', wrong_index)

labels, predict_labels, predict_prob, data_lines_stage3 = stage3_predict()
predict_labels = stage3_helper.output_threshold_for_low_prob(predict_labels, predict_prob, 0.41)
stage3_output(data_lines_stage3, predict_labels)
# print_result('Random Forest', labels, predict_labels)
