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
Had to shape all of the data to the format that I needed. Decided to use x_intercept_left, x_intercept_right, slope_left, slope_right as the data and the commands as the label. Only getting about 60% accuracy at first. Tried 100, 200, 300, 400, 500 sizes for random forest. Melted my computer when I tried 1,000... Thought maybe I should make the commands more uniform, and only have a single pressed and released for each command. Had to devise a way to do this(without manually doing so), took a significant chunk of time.
