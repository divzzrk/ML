
# Machine Learning (ML) Algorithms

* Machine Learning enables computers to learn from data without being explicitly programmed.
* Three types of ML: **Supervised, Unsupervised, and Reinforcement Learning.**

## 1. Supervised Learning
* **Used when output is known** – the algorithm learns from labeled data.
* Two main types: **Regression** and **Classification.**

### Regression
* Predicts continuous values (e.g., predicting house prices, temperature).
* **Algorithms**: 
  * Linear Regression
  * Polynomial Regression
  * Decision Tree Regression
  * Random Forest Regression
  * Support Vector Regression (SVR)

```python
from sklearn.linear_model import LinearRegression
```

#### Key Metrics:
- **Mean Squared Error (MSE)**: Average squared difference between actual and predicted values.
- **R-squared**: Proportion of variance explained by the model.

### Classification
* Predicts categorical outcomes (e.g., classifying email as spam or not).
* **Algorithms**:
  * Logistic Regression
  * K-Nearest Neighbors (KNN)
  * Decision Trees
  * Random Forest Classifier
  * Support Vector Machine (SVM)
  * Naive Bayes

```python
from sklearn.linear_model import LogisticRegression
```

#### Key Metrics:
- **Accuracy**: Proportion of correct predictions.
- **Precision**: True positive rate out of predicted positives.
- **Recall**: True positive rate out of actual positives.
- **F1 Score**: Harmonic mean of precision and recall.

## 2. Unsupervised Learning
* **Used when output is unknown** – the algorithm learns from unlabeled data.
* Two main types: **Clustering** and **Dimensionality Reduction.**

### Clustering
* Groups similar data points together.
* **Algorithms**:
  * K-Means
  * Hierarchical Clustering
  * DBSCAN

```python
from sklearn.cluster import KMeans
```

### Dimensionality Reduction
* Reduces the number of variables to simplify data analysis.
* **Algorithms**:
  * Principal Component Analysis (PCA)
  * Factor Analysis (FA)

```python
from sklearn.decomposition import PCA
```

## 3. Reinforcement Learning
* **Used when the agent learns by interacting with the environment**.
* The agent makes decisions, receives rewards or penalties, and adjusts actions to maximize cumulative reward.

### Key Concepts:
- **Agent**: The learner or decision maker.
- **Environment**: Everything the agent interacts with.
- **Action**: Steps taken by the agent.
- **Reward**: Feedback from the environment based on action.
  
#### Popular Algorithms:
* Q-Learning
* Deep Q-Networks (DQN)
* Policy Gradient Methods

```python
from stable_baselines3 import PPO
```

## Model Evaluation Techniques
* Split the dataset into **training** and **test** sets to evaluate model performance.
* Use **Cross-validation** for robust performance estimates.

```python
from sklearn.model_selection import train_test_split, cross_val_score
```

### Common Evaluation Metrics:
- **Confusion Matrix**: Summarizes predictions into TP, TN, FP, FN.
- **ROC-AUC**: Measures the ability to distinguish between classes.
- **Mean Absolute Error (MAE)**: Measures error in regression models.
