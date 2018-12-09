# picarclassifier

After toying with several different tools and doing a bunch of research, decided to use pandas package to collect data from the csv files given. 
Had to shape all of the data to the format that I needed. Decided to use x_intercept_left, x_intercept_right, slope_left, slope_right as the data and the commands as the label. Only getting about 60% accuracy at first. Tried 100, 200, 300, 400, 500 sizes for random forest. Melted my computer when I tried 1,000... Thought maybe I should make the commands more uniform, and only have a single pressed and released for each command. Had to devise a way to do this(without manually doing so), took a significant chunk of time.
