# corr-1-covid19
Correlation One Data Science for All Women's Summit Project

This project was done as part of the Correlation 1 Data Science for All Women's Summit in March 2020. 

In the wake of the spread of COVID-19 throughout the world,  health call centers are inundated with phone calls, many of which are questions requiring only basic responses.

We aimed to ameliorate this issue by creating a chatbot that could answer these common questions to reduce the load on call centers. 

In essence, it is a chatbot that can detect the intent of a user's question and respond with information straight from the Center for Disease Control or the World Health Organization. 

For EDA, we first scraped coronavirus related tweets from Twitter using their API. We then explored common trends in the data to see what the main concerns and questions were. From there, we formulated our own dataset of commonly asked questions on which to train our model.

To build our model, we tested a multi-class logistic regression model, Ridge regression, Naive Bayes, KNearestNeighbours, and Random Forest Classifiers and found that Ridge regression had the highest F1 scores and accuracy. In the future, we hope to also test a neural network based model.
