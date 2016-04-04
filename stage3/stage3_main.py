import stage3_helper
import stage3_generate_feature
import sklearn
from sklearn import tree

features, labels = stage3_generate_feature.generate_feature('X_training.txt')
features2, labels2 = stage3_generate_feature.generate_feature('X_tuning.txt')

# Decision Tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
predict_labels = clf.predict(features)
predict_labels2 = clf.predict(features2)

print 'Decision Tree: (precision, recall)'
print 'Training Set: ' + str(stage3_helper.accuracy(labels, predict_labels))
print 'Tuning Set: ' + str(stage3_helper.accuracy(labels2, predict_labels2))

