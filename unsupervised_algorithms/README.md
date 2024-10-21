
# Unsupervised ML Algorithms

* Used when output is unknown
* Two types: Dimensionality Reduction & Clustering

## Dimensionality Reduction
* Used when number of variables is more & we need to reduce them.
* Two types - FA and PCA

### Factor Analysis (FA)
* Used to search underlying factors (unobservable variables) also called as factors
* Reduces the set of observed variables to a set of unobservable variables
* Factors - (also called as) - unobservable variables, latent variables, hidden variables, hypothetical variable.
* Two types: EFA and CFA

#### EFA (Exploratory Factor Analysis)
- Basically like lets see what we find

#### CFA (Confirmatory Factor Analysis)
- Basically like lets check our hypothesis

```scikit factor_analyzer library ```

* Before performing FA we need to check if we can perform it on the data
* We need to check the factorability or the sampling adequacy.
* Two tests - Bartletts test and KMO test

#### Bartletts Test of Sphericity
- Observed correlation matrix is compared against indentity matrix (null hypothesis - where we assume all variables are uncorrelated)
- If test is statistically insignificant dont perform FA.
- If p-value < 0.5 --> significant

#### Kasier Meyer Olkin Test (KMO Test)

- Used to measure the sampling adequacy of the dataset
- Estimate proportion of variance among the observed variables
- If KMO > 0.5 --> significant

#### Eigen value

* this is used to determine the optimal number of factors
* it represents the variance explained by each factor.
* high eigen value - the factor has a significant portion in variance in the data
* **kaiser criteria** - we retain the factors having eigen value > 1

#### Factor loadings

* Correlation between the original values and the extracted factors.
* High loading - Variable has strong correlation to the factor.
* Low loading - Variable has weak relation to the factor.

### Principal Component Analysis (PCA)

* Transforms large number of correlated variables to small number of uncorrelated variables called as Principal Components
* Done with least loss of information
* To overcome feature redundancy in the dataset
* The Principal Components should be uncorrelated
* The first component has highest variance followed by 2nd, 3rd,..etc
* Larger the variance captured by first component larger the information captured by it.

```from sklearn.decomposition import PCA```

## Clustering

* Process of organizing objects into groups whose members are similar.
* Finding structure in a collection of unlabelled data
* Data points in a cluster are *homogenous* & *heterogenous* to other clusters.
* Two types - k means & agglomerative Clustering

### K-means
- We need to determine the number of clusters before applying k means Algorithm.
- Pick K number of points called as **centroids**
- Each data point forms a cluster with the nearest centroid
- repeat until convergence -> when centroids doesnt change.

- **WCSS** (within cluster sum of square) = sum of square of differences between each point and the centroid

```sklearn.cluster import KMeans```

### Agglomerative Hierarchical Clustering

- Two types - Top Down and Bottom Up
#### Top Down
- Considers entire dataset as 1 cluster.
- Then breaks down into 2, and continues

#### Bottom Up
- Builds cluster from n to 1
