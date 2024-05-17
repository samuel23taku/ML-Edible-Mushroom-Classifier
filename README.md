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
```

This repository presents two machine learning classification models using logistic regression and k-nearest neighbors (KNN) to classify mushrooms as edible or not edible. 

The logistic regression model achieved an accuracy of 64%, with class-specific precision, recall, and F1-scores indicating moderate performance. 

In contrast, the KNN model demonstrated superior performance with an accuracy of 98%, showcasing high precision, recall, and F1-scores for both classes. 

The repository provides the complete codebase, dataset, and a comprehensive analysis of the results, illustrating the comparative effectiveness of the two models on the mushroom classification task.