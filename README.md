# Principal Component Analysis 

## Goal

To reduce dimensionality, while retaining a large part of variation present in the data.

## Overview

- Is an unsupervised learning method used only for continuous variables.
- Assumes that variables are somewhat correlated.
- Does not involve Hyperparameters.
- Highly affected by outliers.
- Is a nonparametric method.

## Steps for the Algorithm

**Step 1: Center the data**
- Centering or standardizing data

**Step 2: Covariance Matrix**
- Get covariance and variance for variables

**Step 3: Eigenvectors & Eigenvalues**
- Eigendecomposition for covariance matrix

**Step 4: Feature Reduction**
- Keep desired, or all, eigenvectors of principal components

**Step 5: Recast along principal components axes**
- Reorient or project the data from original axes along the principal components

## Descriptive statistics and linear algebra in PCA - A matrix:

- Assume you have a given 5 x 3 matrix with X's as column names and ids as row names.
  - Number of rows = 5
  - Number of columns = 3

$$ A = \begin{bmatrix}  & X1 & X2 & X3 \\ id 1 & 6 & 4 & 4 \\ id 2 & 8 & 3 & 3 \\ id 3 & 5 & 8 & 4 \\ id 4 & 4 & 5 & 10 \\ id 5 & 2 & 8 & 5 \end{bmatrix}$$

- To apply the PCA, we need:

  - Mean values:

  $$ M  = \begin{bmatrix} \bar X1  & \bar X2 & \bar X3 \end{bmatrix} = \begin{bmatrix} 5.0 & 5.6 & 5.2 \end{bmatrix} $$

  - Centering:
    - Subtract the mean from the data 

  $$ C = A - M =  \begin{bmatrix}  & X1 - \bar X1  & X2 - \bar X2 & X3 - \bar X3 \\ id 1 & 1  & -1.6 & -1.2 \\ id 2 & 3  & -2.6 & -2.2 \\ id 3 & 0  & 2.4 & -1.2 \\ id 4 & -1  & -0.6 & 4.8 \\ id 5 & -3  & 2.4 & -0.2 \end{bmatrix} $$

  - Covariance matrix:

  $$ COV = \begin{bmatrix} & X1 - \bar X1 & X2 - \bar X2 & X3 - \bar X3 \\ X1 - \bar X1 & variance(x_{1}) & cov(x_{1},x_{2}) & cov(x_{1},x_{3}) \\ X2 - \bar X2 & cov(x_{2},x_{1}) & variance(x_{2}) & cov(x_{2},x_{3}) \\ X3 - \bar X3 & cov(x_{3},x_{1}) & cov(x_{3},x_{2}) & variance(x_{3})\end{bmatrix} = \begin{bmatrix} & X1 - \bar X1 & X2 - \bar X2 & X3 - \bar X3 \\ X1 - \bar X1 & 5 & -4 & -3 \\ X2 - \bar X2 & -4 & 5.3 & 0.35 \\ X3 - \bar X3 & -3 & 0.35 & 7.7 \end{bmatrix} $$

### Descriptive statistics and linear algebra in PCA - Eigenvectors and Eigenvalues:

- Results for the eigenvalues subtracted from covariance matrix determinant gives us the Eigenvalues scalars, each associated with a principal component.

$$ | \begin{bmatrix} 5 - \lambda & -4 & -3 \\ -4 & 5.3 - \lambda & 0.35 \\ -3 & 0.35 & 7.7 - \lambda \end{bmatrix} | = 0 $$

$$ \lambda = 0.57998089 $$
$$ \lambda = 11.00784433 $$
$$ \lambda = 6.41217478 $$

- With the Eigenvalues we can obtain the eigenvectors.

$$ \begin{bmatrix} 5 - \lambda & -4 & -3 \\ -4 & 5.3 - \lambda & 0.35 \\ -3 & 0.35 & 7.7 - \lambda \end{bmatrix} . \begin{bmatrix} v_{1,1} \\ v_{2,1} \\v_{3,1} \end{bmatrix}  = 0 $$

- For this equation we iteratively plug in each $\lambda$ value to obtain the eigenvectors v.

 For: $\lambda = 0.57998089 $

$$ v_{1} = \begin{bmatrix} 0.74200331 \\ 0.60784646  \\ 0.28276099 \end{bmatrix}$$

 For: $\lambda = 11.00784433 $

$$ v_{2} = \begin{bmatrix} 0.
### Descriptive statistics and linear algebra in PCA - Eigenvectors and Eigenvalues:

- Results for the eigenvalues subtracted from covariance matrix determinant gives us the Eigenvalues scalars, each associated with a principal component.

$$ | \begin{bmatrix} 5 - \lambda & -4 & -3 \\ -4 & 5.3 - \lambda & 0.35 \\ -3 & 0.35 & 7.7 - \lambda \end{bmatrix} | = 0 $$

$$ \lambda = 0.57998089 $$
$$ \lambda = 11.00784433 $$
$$ \lambda = 6.41217478 $$

- With the Eigenvalues we can obtain the eigenvectors.

$$ \begin{bmatrix} 5 - \lambda & -4 & -3 \\ -4 & 5.3 - \lambda & 0.35 \\ -3 & 0.35 & 7.7 - \lambda \end{bmatrix} . \begin{bmatrix} v_{1,1} \\ v_{2,1} \\v_{3,1} \end{bmatrix}  = 0 $$

- For this equation we iteratively plug in each $\lambda$ value to obtain the eigenvectors v.

 For: $\lambda = 0.57998089 $

$$ v_{1} = \begin{bmatrix} 0.74200331 \\ 0.60784646  \\ 0.28276099 \end{bmatrix}$$

 For: $\lambda = 11.00784433 $

$$ v_{2} = \begin{bmatrix} 0.62563791 \\ -0.47632448  \\ -0.61781242 \end{bmatrix}$$

 For: $\lambda = 6.41217478 $

$$ v_{3} = \begin{bmatrix} 0.24084911 \\  -0.63532486  \\ 0.73372613 \end{bmatrix}$$

- The sum of all eigenvalues can be interpreted as the total variance or Inertia of the principal components
$$ TotalVariance(PC) = (\lambda_{1} + \lambda_{2} + \lambda_{3}) = 18 $$

### Descriptive statistics and linear algebra in PCA - Feature Reduction:

- Usually the goal of PCA is to reduce dimensions. Therefore, we will select the amount of eigenvectors that reduces our initial number of columns. 

- We started with 3 columns, so let's reduce to 2 columns. To do so, we need to sort the Eigenvalues from highest to lowest, select the 2 highest and keep their associated Eigenvectors.

 For: $\lambda_{2} = 11.00784433 $

$$ v_{2} = \begin{bmatrix} 0.62563791 \\ -0.47632448  \\ -0.61781242 \end{bmatrix}$$

 For: $\lambda_{3} = 6.41217478 $

$$ v_{3}= \begin{bmatrix} 0.24084911 \\  -0.63532486  \\ 0.73372613 \end{bmatrix}$$

- The Ratio of variance explained by each principal component can be seen as each individual eigenvalue selected over the total variance.

    $$ \frac{[11.00784433 , 6.41217478]}{18} = [0.61154691, 0.35623193] $$

- The total variance % captured by the dimensionality reduction is the sum of the ratios times 100.

     $$ (0.61154691 + 0.35623193)*100   = 96.77  $$

### Descriptive statistics and linear algebra in PCA - transformed data, loadings, and reconstruction:

- To project the data into the principal components, we need to dot multiply the centered data with the reduced eigenvector matrix.

    $$ C.[v_{2},v_{3}] = ProjectedData $$

    $$ \begin{bmatrix} 1  & -1.6 & -1.2 \\ 3  & -2.6 & -2.2 \\ 0  & 2.4 & -1.2 \\ -1  & -0.6 & 4.8 \\ -3  & 2.4 & -0.2 \end{bmatrix} . \begin{bmatrix} 0.62563791 & 0.24084911 \\ -0.47632448 & -0.63532486 \\ -0.61781242 & 0.73372613 \end{bmatrix} = \begin{bmatrix} 2.129132 & 0.376898 \\ 4.474545 & 0.760194 \\ -0.401804 & -2.405251 \\ -3.305343 & 3.662231 \\ -2.
896530 & -2.394072 \end{bmatrix} $$

 - To understand the contribution of the original variables to the projected data, we calculate the loadings as the reduced eigenvector matrix times the square root of the Eigenvalues.

    $$ [v_{2},v_{3}] * [\sqrt \lambda_{2},\sqrt \lambda_{3}] = Loadings $$

    $$ \begin{bmatrix} 0.62563791 & 0.24084911 \\ -0.47632448 & -0.63532486 \\ -0.61781242 & 0.73372613 \end{bmatrix} . \begin{bmatrix} \sqrt{11.00784433} & \sqrt{6.41217478} \end{bmatrix} = \begin{bmatrix} 2.07574595 & 0.60988467 \\ -1.58035278 & -1.6087869 \\ -2.04978247 & 1.85796129 \end{bmatrix} $$   

- We could reconstruct back the original data using the transpose of all Eigenvectors dot multiplied by the completed projected data and then adding the average to that result.

   $$ (v \times ProjectedData)^T + M = OriginalData $$
   $$ \begin{bmatrix} 1  & -1.6 & -1.2 \\ 3  & -2.6 & -2.2 \\ 0  & 2.4 & -1.2 \\ -1  & -0.6 & 4.8 \\ -3  & 2.4 & -0.2 \end{bmatrix} + \begin{bmatrix} 5 & 5.6 & 5.2 \end{bmatrix} = \begin{bmatrix}  6 & 4 & 4 \\ 8 & 3 & 3 \\  5 & 8 & 4 \\  4 & 5 & 10 \\  2 & 8 & 5 \end{bmatrix} $$

# Vars_Samples_Plot.py

This Python script provides functionalities to generate PCA (Principal Component Analysis) plots based on projected data and loadings. It is flexible and can be customized using various parameters.

## Libraries
- `pandas`
- `pandas.api.types`
- `matplotlib`
- `matplotlib.cm`

## Function

- `def vars_samples_plot(ProjectedData, Loadings, ExplainedVar, **kwargs):` Generates a PCA plot based on the given projected data, loadings, and explained variances.

## Optional Parameters:
ProjectedData: (pd.DataFrame) - The projected data.
Loadings: (pd.DataFrame) - The loadings data.
ExplainedVar: (list) - Explained variance for the components.
Optional Parameters (kwargs):
Fig_size: Figure size (default is (16, 12))
Fig_size_sub: Figure size for subplots (default is (20, 12))
Overlaid: Flag to overlay plots or not (default is True)
Plot_style: Style of the plot (default is 'seaborn-whitegrid')
Color_by_disc_var: Column of discrete variable to color by (default is None)
Sample_colors: Colors for samples (default is 'blue')
Sample_size: Size of the sample points (default is 15)
Sample_labels: Flag to show sample labels or not (default is True)
Sample_labels_color: Color for sample labels (default is 'black')
Sample_labels_size: Size of the sample labels (default is 10)
Sample_labels_shift: Shift for sample labels (default is .02)
Arrow_colors: Color of the arrows (default is 'red')
Arrow_head_size: Size of the arrow heads (default is 0.05)
Arrow_labels: Flag to show arrow labels or not (default is True)
Arrow_labels_size: Size of the arrow labels (default is 10)
Arrow_labels_color: Color of the arrow labels (default is 'black')
Arrow_labels_shift: Shift for arrow labels (default is 1.15)
X_label_size: Size of the X-axis label (default is 15)
Y_label_size: Size of the Y-axis label (default is 15)
Title_size: Size of the title (default is 20)

## Features:

- `Error Handling for Dependencies: The script will check for the existence of necessary libraries and prompt the user to install them if they're missing.`
- `Flexibility through Optional Parameters: Multiple optional parameters allow users to customize the PCA plot's appearance.`
- `Support for Overlaying Plots: Users can decide to overlay the samples and loadings plots or display them side by side.`
- `Conditional Coloring based on Discrete Variables: If provided, the plot can color samples based on the discrete variables' values.`
- `Dynamic Labeling: The script supports dynamic labeling based on the actual values of the projected data, loadings, and explained variances.`
- `Arrow Representations for Loadings: Loadings are represented as arrows, pointing in the direction and magnitude of the loading.`

## Usage:
- After ensuring the required libraries are installed, you can call the function vars_samples_plot with the required parameters and desired optional parameters to generate the PCA plot.
