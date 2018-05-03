import os
import pickle
from sklearn.ensemble import RandomForestClassifier

def forest_predictor(file_path,number, **kwargs):
    save = kwargs.get('save', False)
    test = kwargs.get('test', False)
    if not file_path.endswith('.csv'):
        return
    with open(file_path, 'r') as infile:
        two_d = [line.replace('\n', '').split(',') for line in infile]

    if kwargs.get('header', False):
        two_d = two_d[1:]

    if (number == 0):
        new_d = [line[1:] for line in two_d]
        class_col = [line[0] for line in two_d]
    else:
        new_d = [line[:-1] for line in two_d]
        class_col = [line[-1] for line in two_d]
    if save:
        if os.path.isfile(save):
            with open(save, 'rb') as infile:
                clf = pickle.load(infile)
        else:
            clf = RandomForestClassifier(n_estimators=500)
            clf = clf.fit(new_d, class_col)
            with open(save, 'wb') as outfile:
                pickle.dump(clf, outfile)
    else:
        clf = RandomForestClassifier(n_estimators=500)
        clf = clf.fit(new_d, class_col)

    if test:
         print(clf.predict(kwargs.get('test')))
         return clf



if __name__ == '_main_':
    x = [[15,0], [18,60000], [80,30000]]
    clf = forest_predictor('test_files/simple_data.csv', 2, header=True, save='saves/random_forest.p', test=x)
    print(clf.feature_importances_)