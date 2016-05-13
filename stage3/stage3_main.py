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


features_X, labels_X, data_lines = stage3_generate_feature.generate_feature('Y.txt')

skf = StratifiedKFold(labels_X, 5)


def train_model(model, loss, learning_rate, n_estimators, max_depth, max_features):
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

        clf = model(n_estimators=n_estimators, loss=loss, learning_rate=learning_rate,
                    max_depth=max_depth, max_features=max_features)
        # clf = model()
        clf = clf.fit(features_train, labels_train)
        predict_labels_test = clf.predict(features_test)
        predict_labels_prob = clf.predict_proba(features_test)

        # for i in range(0, len(test)):
        #     if stage3_hand_code_rule.hand_code_rule(data_lines[test[i]]) is not None:
        #         predict_labels_test[i] = stage3_hand_code_rule.hand_code_rule(data_lines[test[i]])

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


def stage3_predict(model):
    features_test, labels_test, data_lines_3 = stage3_generate_feature.generate_feature('Y.txt')
    # features_test, labels_test, data_lines_3 = stage3_generate_feature.generate_feature('Y.txt')
    clf = model(n_estimators=1000)
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
# # clf = tree.DecisionTreeClassifier()  # TODO: add parameters
# labels, predict_labels, wrong_index, predict_prob = train_model(tree.DecisionTreeClassifier)
# stage3_helper.print_result('Decision Tree', labels, predict_labels)
#
# # # Random Forest
# # labels, predict_labels, wrong_index = train_model(ensemble.RandomForestClassifier)
# # print_result('Random Forest', labels, predict_labels)
#
# # Gaussian Naive Bayes
# labels, predict_labels, wrong_index, predict_prob = train_model(naive_bayes.GaussianNB)
# stage3_helper.print_result('Gaussian Naive Bayes', labels, predict_labels)
#
# # Multinomial Naive Bayes
# labels, predict_labels, wrong_index, predict_prob = train_model(naive_bayes.MultinomialNB)
# stage3_helper.print_result('Multinomial Naive Bayes', labels, predict_labels)
#
# # Bernoulli Naive Bayes
# labels, predict_labels, wrong_index, predict_prob = train_model(naive_bayes.BernoulliNB)
# stage3_helper.print_result('Bernoulli Naive Bayes', labels, predict_labels)

# # SVM-SVC
# labels, predict_labels, wrong_index, predict_prob = train_model(svm.SVC)
# stage3_helper.print_result('SVM-SVC', labels, predict_labels)
#
# # SVM-NuSVC
# labels, predict_labels, wrong_index, predict_prob = train_model(svm.NuSVC)
# stage3_helper.print_result('SVM-NuSVC', labels, predict_labels)

# # Logistic Regression
# labels, predict_labels, wrong_index, predict_prob = train_model(linear_model.LogisticRegression)
# stage3_helper.print_result('Logistic Regression', labels, predict_labels)




labels, predict_labels, wrong_index, predict_prob = train_model(ensemble.GradientBoostingClassifier,
                                                                'deviance', 0.05, 1000,
                                                                7, None)
for threshold in numpy.arange(0.2, 0.6, 0.01):
    print 'Threshold:', threshold
    predict_labels = stage3_helper.output_threshold_for_low_prob(predict_labels, predict_prob, threshold)
    stage3_helper.print_result('Random Forest', labels, predict_labels)
# stage3_helper.print_result('GradientBoostingClassifier', labels, predict_labels)
# stage3_hand_code_rule.print_wrong_data('X.txt', wrong_index)


# for Loss in ['deviance']:
#     for Learning_rate in [0.03, 0.04, 0.05, 0.06, 0.07, 0.08]:
#         for N_estimators in [1000]:
#             for Max_depth in [7]:
#                 for Max_features in [None]:
#                     print Loss, Learning_rate, N_estimators, Max_depth, Max_features
#                     labels, predict_labels, wrong_index, predict_prob = train_model(ensemble.GradientBoostingClassifier,
#                                                                                     Loss, Learning_rate, N_estimators,
#                                                                                     Max_depth, Max_features)
#                     stage3_helper.print_result('GradientBoostingClassifier', labels, predict_labels)

# labels, predict_labels, predict_prob, data_lines_stage3 = stage3_predict()
# predict_labels = stage3_helper.output_threshold_for_low_prob(predict_labels, predict_prob, 0.41)
# stage3_output(data_lines_stage3, predict_labels)
# stage3_helper.print_result('Random Forest', labels, predict_labels)
