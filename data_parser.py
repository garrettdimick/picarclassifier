import pandas as pd
from sklearn.model_selection import train_test_split

def collect_data():
    data_set_0 = pd.read_csv("PI_CAR_DATA/PI_Car_Runs0.csv")
    data_set_1 = pd.read_csv("PI_CAR_DATA 2/PI_Car_Runs2.csv")
    data_set_2 = pd.read_csv("PI_CAR_DATA 3/PI_Car_Runs3.csv")
    s = pd.Series(data_set_0['Commands'])
    for i in xrange(0, len(s)):
        split = s.get(i).split(',')
        split2 = split[0].split(' ')
        val = split2[0] + ' pressed, ' + split2[0] + ' released'
        data_set_0.set_value(i, 'Commands', val)

    s = pd.Series(data_set_1['Commands'])
    for i in xrange(0, len(s)):
        split = s.get(i).split(',')
        split2 = split[0].split(' ')
        val = split2[0] + ' pressed, ' + split2[0] + ' released'
        data_set_1.set_value(i, 'Commands', val)

    s = pd.Series(data_set_2['Commands'])
    for i in xrange(0, len(s)):
        split = s.get(i).split(',')
        split2 = split[0].split(' ')
        val = split2[0] + ' pressed, ' + split2[0] + ' released'
        data_set_2.set_value(i, 'Commands', val)

    data_frames = [data_set_0, data_set_1, data_set_2]

    data = pd.concat(data_frames)

    x_data = data[['X_Intercept_Left', 'X_Intercept_Right', 'Slope_Left', 'Slope_Right']]  # features
    y_data = data['Commands']  # labels

    x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.05)

    return x_train, x_test, y_train, y_test

