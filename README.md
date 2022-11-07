**Background**
---
Home Credit has a problem where it requires efficiency and speed in receiving loans from each customer. As a Data Science Intern from Home Credit, we will to process data and create models that are able to predict and assess optimal credit applications and predict credit score customer. To facilitate the predicition, we will create a credit scorecard based on the logistic regression model. Finally, we will provide solutions for lending companies how the insights we get.

**Data Pre-processing**
---
1. Handling Missing Value
2. Feature Selection based information value from scorecardpy
3. Feature Engineering to bin using Weight of Evidence and Information Value from scorecardpy
4.  Imbalance Data Handling

**Modelling**
---
1. Evaluation target is AUC Score 
2. Logistic Regression Model are tested with hyperparameter tuning result to get best AUC Score value
3. Logistic Regression with hyperparameter tuning get better result where the AUC Score value obtained is 73.04%
4. Generated best model using Logistic Regression with score 0.34 on Kolmogorov–Smirnov (KS - Statistic).
![AUC   KS](https://user-images.githubusercontent.com/68262798/200212973-3006a673-af71-4985-a682-adc2edc5193d.png)
![AUC   KS Test](https://user-images.githubusercontent.com/68262798/200213743-239950ab-0513-4759-aa4d-a1b114223b1e.png)


**Credit Score**
---
1. Obtain scorecard each feature based on coefficient of Logistic Regression
2. Show scorecard feature that can boost credit score customer and can reduce credit score customer
3. Simulation predict from our model deployed on streamlit. Simulation will predict how much credit score each customer get based on scorecard and is application credit will approved or rejected. 

**Simulation Credit Score Predicition [Here](https://audryannoor-home-credit-vix-streamlitapp-c7h57p.streamlit.app/)**
