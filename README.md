# picarclassifier

After toying with several different tools and doing a bunch of research, decided to use pandas package to collect data from the csv files given. 
Only getting 10% accuracy after my initial method, which included trying a bunch of things like this to get the data to the way that I wanted:
```python
data_set_0 = data_set_0[data_set_0['X_Intercept_Left'].apply(lambda x: pd.to_numeric(x))]
    data_set_1 = data_set_1[data_set_1['X_Intercept_Left'].apply(lambda x: pd.to_numeric(x))]
    data_set_2 = data_set_2[data_set_2['X_Intercept_Left'].apply(lambda x: not isinstance(x, (str)))]
```
and
```python
    data_set_0[['X_Intercept_Left', 'X_Intercept_Right', 'Slope_Left', 'Slope_Right']] = \
        data_set_0[['X_Intercept_Left', 'X_Intercept_Right', 'Slope_Left', 'Slope_Right']].apply(pd.to_numeric)
    data_set_1[['X_Intercept_Left', 'X_Intercept_Right', 'Slope_Left', 'Slope_Right']] = \
        data_set_1[['X_Intercept_Left', 'X_Intercept_Right', 'Slope_Left', 'Slope_Right']].apply(pd.to_numeric)
    data_set_2[['X_Intercept_Left', 'X_Intercept_Right', 'Slope_Left', 'Slope_Right']] = \
        data_set_2[['X_Intercept_Left', 'X_Intercept_Right', 'Slope_Left', 'Slope_Right']].apply(pd.to_numeric)
```
Had to shape all of the data to the format that I needed. Decided to use x_intercept_left, x_intercept_right, slope_left, slope_right as the feature data and the commands as the label. Only getting about 60% accuracy at first. Tried 100, 200, 300, 400, 500 sizes for random forest. Melted my computer when I tried 1,000... Thought maybe I should make the commands more uniform, and only have a single pressed and released for each command. Had to devise a way to do this(without manually doing so), took a significant chunk of time. Tried regex, manually changing (abandoned that early), etc. I ended up finding the first command seen from the commands column, and turning it into a press and release of whichever direction that command contained. For example, 
``` right released,right pressed,right released,right pressed,right released ``` became simply ```right pressed, right released```. I made this decision because I assume that several commands are a product of minor adjustments from the operator. I also believe that having less potential labels will help the classifier make better decisions. For the most part really long commands don't make sense to me, so I reduced them to simpler ones.
After finally figuring this out, taking a sort of naive approach, trained classifier again. Got 84% accuracy on 100 tree Random Forest. 83% for 200. 84% for 300. 84% for 400. 83% for 500. Got 88% for 1,000. I wasn't expecting to see any increase in the accuracy of the model by increasing the number of trees. I think it was a coincidence, didn't see any improvement on several more attempts with 1,000 trees. After several more I got values between 80 and 90% accuracy.
Wanted to maybe tweak some parameters to see if I could improve performance. Also wanted to see which features are the most important, because I am not so sure that the x intercept values are as important as the slope values.
I used the feature importances variable from scikit learn to do the following:
```python
    feature_imp = pd.Series(clf.feature_importances_, index=['X_Intercept_Left', 'X_Intercept_Right', 'Slope_Left', 'Slope_Right']).sort_values(ascending=False)
print feature_imp
```
which produced the output
```
X_Intercept_Right    0.272514
Slope_Right          0.255111
X_Intercept_Left     0.248655
Slope_Left           0.223719
dtype: float64
``` 
This did not support my thought that the slopes were more important that the left and right x intercepts.

Next, in an attempt to improve the accuracy of the classifier, I tried Random Search Cross Validation, which is RandomizedSearchCV in sklearn. This allows for some (kind of) systematic, random hyperparameter tuning. From this, I found the best hyperparameters to tune using best_params_. 
best_params_ are {'n_estimators': 611, 'min_samples_split': 2, 'bootstrap': True, 'max_depth': None, 'min_samples_leaf': 1}
The random search grid only provided about a 2% increase from the average accuracy I had been getting with no parameter tuning. Began training some classifiers with the newly discovered "best parameters." The accuracy of the classifier trained with the "best parameters" was 86.38 percent, and the classifier I trained with no tuning at all alongside it got an accuracy of 86.8 percent. At this point, I determined that I was probably no longer going to get more benefits from tuning parameters, at least with how slow my machine is. The best thing to do to make my classifier more accurate would be to collect more data and train it on that data. I think that random forests are a viable option for this type of classification, and hopefully it won't drive the picar off of a bridge or anything.

In order to run the code: 
If inside RF_tester.py:
Change the filepath variable on line 3 in RF_tester.py
If not, you can import RF_tester and use the methods defined in RF_tester.py to get commands for the picar from a classifier.
Next, you can do one of two things: 
1. call load_forest(classifier_path) with your newly set path, then call make_decision(left_x_int, right_x_int, left_slope, right_slope, classifier) and pass it the classifier that is loaded by load_forest, this will make a prediction.
or
2. call load_classifier_make_decision(left_x_int, right_x_int, left_slope, right_slope, classifier_path), which will load the classifier from the given path and make a prediction.

Both of these methods return a tuple of two string values which can be given to the picar_key_receiver:
('up pressed', 'up released'),  ('down pressed, down released'), ('left pressed, left released'), ('right pressed, right released')
