import stage3_helper
import stage3_generate_feature
import stage3_hand_code_rule
from sklearn import tree
from sklearn import ensemble
from sklearn import naive_bayes
from sklearn import svm
from sklearn import linear_model
from sklearn.cross_validation import StratifiedKFold


features_X, labels_X = stage3_generate_feature.generate_feature('X.txt')

skf = StratifiedKFold(labels_X, 5)


def train_model():
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

        clf = ensemble.RandomForestClassifier(n_estimators=1000)  # TODO: add parameters
        clf = clf.fit(features_train, labels_train)
        predict_labels_test = clf.predict(features_test)

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
# predict_labels_training, predict_labels_tuning = train_model(clf)
# print_result('Decision Tree', predict_labels_training, predict_labels_tuning)

# Random Forest
# clf = ensemble.RandomForestClassifier(n_estimators=1000)  # TODO: add parameters
# predict_labels_training, predict_labels_tuning = train_model(clf)
# print_result('Random Forest', predict_labels_training, predict_labels_tuning)

# # Gaussian Naive Bayes
# clf = naive_bayes.GaussianNB()  # TODO: add parameters
# predict_labels_training, predict_labels_tuning = train_model(clf)
# print_result('Gaussian Naive Bayes', predict_labels_training, predict_labels_tuning)
#
# # Multinomial Naive Bayes
# clf = naive_bayes.MultinomialNB()  # TODO: add parameters
# predict_labels_training, predict_labels_tuning = train_model(clf)
# print_result('Multinomial Naive Bayes', predict_labels_training, predict_labels_tuning)
#
# # Bernoulli Naive Bayes
# clf = naive_bayes.BernoulliNB()  # TODO: add parameters
# predict_labels_training, predict_labels_tuning = train_model(clf)
# print_result('Bernoulli Naive Bayes', predict_labels_training, predict_labels_tuning)
#
# # SVM-SVC
# clf = svm.SVC()  # TODO: add parameters
# predict_labels_training, predict_labels_tuning = train_model(clf)
# print_result('SVM-SVC', predict_labels_training, predict_labels_tuning)
#
# # SVM-NuSVC
# clf = svm.NuSVC()  # TODO: add parameters
# predict_labels_training, predict_labels_tuning = train_model(clf)
# print_result('SVM-NuSVC', predict_labels_training, predict_labels_tuning)
#
# # Logistic Regression
# clf = linear_model.LogisticRegression()  # TODO: add parameters
# predict_labels_training, predict_labels_tuning = train_model(clf)
# print_result('Logistic Regression', predict_labels_training, predict_labels_tuning)

labels, predict_labels, wrong_index = train_model()
print_result('Random Forest', labels, predict_labels)

stage3_hand_code_rule.print_wrong_data('X.txt', wrong_index)
