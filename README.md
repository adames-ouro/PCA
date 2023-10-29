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

## PCA math:

- Math explained in notebook named `Dimensionality Reduction - PCA.ipynb`


# Vars_Samples_Plot.py

This Python script provides functionalities to generate PCA (Principal Component Analysis) plots based on projected data and loadings. It is flexible and can be customized using various parameters.

## Libraries
- `pandas`
- `matplotlib`

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
