import stage3_helper
import stage3_generate_feature
from sklearn import tree
from sklearn import ensemble
from sklearn import naive_bayes
from sklearn import svm
from sklearn import linear_model


features_training, labels_training = stage3_generate_feature.generate_feature('X_training.txt')
features_tuning, labels_tuning = stage3_generate_feature.generate_feature('X_tuning.txt')


def train_model(current_clf):
    current_clf = current_clf.fit(features_training, labels_training)
    current_predict_labels_training = current_clf.predict(features_training)
    current_predict_labels_tuning = current_clf.predict(features_tuning)
    return current_predict_labels_training, current_predict_labels_tuning


def print_result(model_name, current_predict_labels_training, current_predict_labels_tuning):
    print model_name
    print 'Result:        ' + '(precision, recall)'
    print 'Training Set:  ' + str(stage3_helper.accuracy(labels_training, current_predict_labels_training))
    print 'Tuning Set:    ' + str(stage3_helper.accuracy(labels_tuning, current_predict_labels_tuning))
    print ''


# Decision Tree
clf = tree.DecisionTreeClassifier()  # TODO: add parameters
predict_labels_training, predict_labels_tuning = train_model(clf)
print_result('Decision Tree', predict_labels_training, predict_labels_tuning)

# Random Forest
clf = ensemble.RandomForestClassifier()  # TODO: add parameters
predict_labels_training, predict_labels_tuning = train_model(clf)
print_result('Random Forest', predict_labels_training, predict_labels_tuning)

# Gaussian Naive Bayes
clf = naive_bayes.GaussianNB()  # TODO: add parameters
predict_labels_training, predict_labels_tuning = train_model(clf)
print_result('Gaussian Naive Bayes', predict_labels_training, predict_labels_tuning)

# Multinomial Naive Bayes
clf = naive_bayes.MultinomialNB()  # TODO: add parameters
predict_labels_training, predict_labels_tuning = train_model(clf)
print_result('Multinomial Naive Bayes', predict_labels_training, predict_labels_tuning)

# Bernoulli Naive Bayes
clf = naive_bayes.BernoulliNB()  # TODO: add parameters
predict_labels_training, predict_labels_tuning = train_model(clf)
print_result('Bernoulli Naive Bayes', predict_labels_training, predict_labels_tuning)

# SVM-SVC
clf = svm.SVC()  # TODO: add parameters
predict_labels_training, predict_labels_tuning = train_model(clf)
print_result('SVM-SVC', predict_labels_training, predict_labels_tuning)

# SVM-NuSVC
clf = svm.NuSVC()  # TODO: add parameters
predict_labels_training, predict_labels_tuning = train_model(clf)
print_result('SVM-NuSVC', predict_labels_training, predict_labels_tuning)

# Logistic Regression
clf = linear_model.LogisticRegression()  # TODO: add parameters
predict_labels_training, predict_labels_tuning = train_model(clf)
print_result('Logistic Regression', predict_labels_training, predict_labels_tuning)
