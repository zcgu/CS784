import stage3_helper
import stage3_generate_feature
import stage3_hand_code_rule
from sklearn import tree
from sklearn import ensemble
from sklearn import naive_bayes
from sklearn import svm
from sklearn import linear_model
from sklearn.cross_validation import StratifiedKFold


features_X, labels_X, data_lines = stage3_generate_feature.generate_feature('Y.txt')

skf = StratifiedKFold(labels_X, 5)


def train_model(model):
    labels = []
    predict_labels = []
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

        for i in range(0, len(test)):
            if stage3_hand_code_rule.hand_code_rule(data_lines[test[i]]) is not None:
                predict_labels_test[i] = stage3_hand_code_rule.hand_code_rule(data_lines[test[i]])

        for label in labels_test:
            labels.append(label)
        for label in predict_labels_test:
            predict_labels.append(label)

        for i in range(0, len(labels_test)):
            if labels_test[i] != predict_labels_test[i]:
                wrong_index.append(test[i])
    return labels, predict_labels, wrong_index


def print_result(model_name, labels, predict_labels):
    print model_name
    print 'Result:' + '(precision, recall)'
    print str(stage3_helper.accuracy(labels, predict_labels))
    print ''


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

labels, predict_labels, wrong_index = train_model(ensemble.RandomForestClassifier)
print_result('Random Forest', labels, predict_labels)

stage3_hand_code_rule.print_wrong_data('X.txt', wrong_index)
