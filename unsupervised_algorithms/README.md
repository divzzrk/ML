
# Unsupervised ML Algorithms

* Used when output is unknown
* Two types: Dimensionality Reduction & Clustering

## Dimensionality Reduction
* Used when the number of variables is high, and we need to reduce them.
* Two types - **Factor Analysis (FA)** and **Principal Component Analysis (PCA)**

### Factor Analysis (FA)
* Used to search for underlying factors (unobservable variables) also called **factors**
* Reduces the set of observed variables to a set of unobservable variables
* Factors - also known as unobservable variables, latent variables, hidden variables, or hypothetical variables.
* Two types: **EFA** and **CFA**

#### EFA (Exploratory Factor Analysis)
- Basically like "let's see what we find."

#### CFA (Confirmatory Factor Analysis)
- Basically like "let's check our hypothesis."

```python
from factor_analyzer import FactorAnalyzer
```

* Before performing FA, we need to check if we can perform it on the data.
* We need to check the **factorability** or the **sampling adequacy**.
* Two tests - **Bartlett's Test** and **KMO Test**

#### Bartlett's Test of Sphericity
- The observed correlation matrix is compared against the identity matrix (null hypothesis assumes all variables are uncorrelated).
- If the test is statistically insignificant, don't perform FA.
- If p-value < 0.05 → significant.

#### Kaiser-Meyer-Olkin Test (KMO Test)
- Used to measure the sampling adequacy of the dataset.
- Estimates the proportion of variance among the observed variables.
- If KMO > 0.5 → significant.

#### Eigenvalue
* This is used to determine the optimal number of factors.
* It represents the variance explained by each factor.
* High eigenvalue → the factor has a significant contribution to the variance in the data.
* **Kaiser Criteria**: Retain factors having an eigenvalue > 1.

#### Factor Loadings
* The correlation between the original variables and the extracted factors.
* High loading → variable has a strong correlation to the factor.
* Low loading → variable has a weak relation to the factor.

### Principal Component Analysis (PCA)
* Transforms a large number of correlated variables into a smaller number of uncorrelated variables called **Principal Components**.
* Done with the least loss of information.
* Helps overcome feature redundancy in the dataset.
* The Principal Components should be uncorrelated.
* The first component has the highest variance, followed by the 2nd, 3rd, etc.
* The larger the variance captured by the first component, the more information it contains.

```python
from sklearn.decomposition import PCA
```

## Clustering
* The process of organizing objects into groups whose members are similar.
* Used to find structure in a collection of unlabelled data.
* Data points in a cluster are **homogeneous** & **heterogeneous** to other clusters.
* Two types: **K-Means** & **Agglomerative Clustering**

### K-Means
- The number of clusters (K) needs to be determined before applying the K-Means algorithm.
- Pick K number of points called **centroids**.
- Each data point forms a cluster with the nearest centroid.
- Repeat until convergence → when centroids no longer change.

- **WCSS** (Within Cluster Sum of Squares): Sum of the square of differences between each point and the centroid.

```python
from sklearn.cluster import KMeans
```

### Agglomerative Hierarchical Clustering
- Two types: **Top Down** and **Bottom Up**

#### Top Down
- Considers the entire dataset as 1 cluster.
- Then breaks down into 2, and continues.

#### Bottom Up
- Builds clusters from N clusters down to 1.
