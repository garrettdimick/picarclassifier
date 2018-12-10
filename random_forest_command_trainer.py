import pandas as pd
import numpy as np
import cPickle
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree, metrics
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import GridSearchCV

from data_parser import collect_data

FILE_PATH = '/Users/garrettdimick/5600final/models/randomforest.pck'


def save_forest(forest, file_name):
    with open(file_name, 'wb') as f:
        cPickle.dump(forest, f)

x_train, x_test, y_train, y_test = collect_data()

## FOR HYPERPARAMETER TUNING

# n_estimators = [int(x) for x in np.linspace(start=500, stop=1000, num=10)]
# max_depth = [int(x) for x in np.linspace(10, 100, num=10)]
# max_depth.append(None)
# min_samples_split = [2, 5, 10]
# min_samples_leaf = [1, 2, 4]
# bootstrap = [True, False]
#
# random_grid = {'n_estimators': n_estimators,
#                'max_depth': max_depth,
#                'min_samples_split': min_samples_split,
#                'min_samples_leaf': min_samples_leaf,
#                'bootstrap': bootstrap}
# print random_grid

# clf = RandomForestClassifier()
# clf_random_search = RandomizedSearchCV(estimator=clf, param_distributions=random_grid, n_iter=50, cv=2)
#
# clf_random_search.fit(x_train, y_train)
# print clf_random_search.best_params_
# save_forest(clf_random_search, FILE_PATH)
# y_pred_random_search = clf_random_search.predict(x_test)


clf = RandomForestClassifier(1000)
clf.fit(x_train, y_train)
save_forest(clf, FILE_PATH)
y_pred = clf.predict(x_test)


# clf = RandomForestClassifier(n_estimators=611, min_samples_split=2, bootstrap=True, max_depth=None, min_samples_leaf=1)
# clf.fit(x_train, y_train)
# save_forest(clf, FILE_PATH)
# y_pred_tuned = clf.predict(x_test)

print "Accuracy: ", metrics.accuracy_score(y_test, y_pred)
# print "Accuracy with random search: ", metrics.accuracy_score(y_test, y_pred_random_search)
# print "Tuned accuracy: ", metrics.accuracy_score(y_test, y_pred_tuned)

