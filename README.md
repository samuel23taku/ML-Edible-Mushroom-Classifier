# Edible mushrooms classifier - Log Regression

# 1. Dataset Overview

DataSource https://www.kaggle.com/datasets/prishasawhney/mushroom-dataset/data

```
This data set contains 9 columns:
- Cap Diameter
- Cap Shape
- Gill Attachment
- Gill Color
- Stem Height
- Stem Width
- Stem Color
- Season
- Target Class - Is it edible or not?

The Target Class contains two values - 0 or 1 - where 0 refers to edible and 1 refers to poisonous.

```
# 2. Technical Requirements

**Libraries**
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

# 3. Algorithms
- Logistic Regression
- K-Nearest Neighbors
- SVM with RBF kernel
- Decision Tree

# 3. Results

```
Logistic Regression:

Precision: 0.61 (class 0), 0.66 (class 1)
Recall: 0.56 (class 0), 0.71 (class 1)
F1-Score: 0.58 (class 0), 0.68 (class 1)
Accuracy: 0.64

KNN:

Precision: 0.97 (class 0), 0.99 (class 1)
Recall: 0.99 (class 0), 0.97 (class 1)
F1-Score: 0.98 (class 0 and 1)
Accuracy: 0.98

Decision Tree

              precision    recall  f1-score   support

           0       0.97      0.96      0.97      7308
           1       0.97      0.98      0.97      8903

    accuracy                           0.97     16211
   macro avg       0.97      0.97      0.97     16211
weighted avg       0.97      0.97      0.97     16211


SVM:

              precision    recall  f1-score   support

           0       0.98      0.97      0.97     20706
           1       0.98      0.98      0.98     25224

    accuracy                           0.98     45930
   macro avg       0.98      0.98      0.98     45930
weighted avg       0.98      0.98      0.98     45930
```

This repository presents two machine learning classification models using logistic regression and k-nearest neighbors (KNN) to classify mushrooms as edible or not edible. 

The logistic regression model achieved an accuracy of 64%, with class-specific precision, recall, and F1-scores indicating moderate performance. 

The KNN model demonstrated superior performance with an accuracy of 98%, showcasing high precision, recall, and F1-scores for both classes. 

The SVM model has an accuracy of 98%, but it could probably do better with more compute. 

The repository provides the complete codebase, dataset, and a comprehensive analysis of the results, illustrating the comparative effectiveness of the two models on the mushroom classification task.