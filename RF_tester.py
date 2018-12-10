import cPickle

FILE_PATH = '/Users/garrettdimick/5600final/models/randomforest87pct.pck'


def load_forest(classifier_path):
    with open(classifier_path, 'rb') as f:
        clf = cPickle.load(f)
    return clf


def load_classifier_make_decision(left_x_int, right_x_int, left_slope, right_slope, classifier_path):
    clf = load_forest(classifier_path)
    dec = str(clf.predict([[left_x_int, right_x_int, left_slope, right_slope]]))
    decision1, decision2 = dec[2:-2].split(", ")
    return decision1, decision2


def make_decision(left_x_int, right_x_int, left_slope, right_slope, classifier):
    dec = str(classifier.predict([[left_x_int, right_x_int, left_slope, right_slope]]))
    decision1, decision2 = dec[2:-2].split(", ")
    return decision1, decision2


def unit_test_01(file_path):
    next_move = load_classifier_make_decision(0, 0, 0, 0, file_path)
    print next_move


def unit_test_02():
    clf = load_forest(FILE_PATH)
    next_move = make_decision(169, 172, -1, 10.4801188, clf)
    print next_move
    next_move = make_decision(57, 232, -2.325868444, 34.88253968, clf)
    print next_move
    next_move = make_decision(81, 203, -2.992131542, 10.83212379, clf)
    print next_move
    next_move = make_decision(117, 243, -6.3743949, 3.1888139, clf)
    print next_move
    next_move = make_decision(97, 265, -5.4201789, 3.50056985, clf)
    print next_move

# unit_test_01(FILE_PATH)
# unit_test_02()