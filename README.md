# Data Analysis (Cross-validation Technique)
![Python 3.7](https://img.shields.io/badge/Python-3.7-brightgreen.svg) 

• Please do ⭐ the repository, if it helped you in anyway.

  There are many different ways one can do cross-validation, and it is the most critical
step when it comes to building a good machine learning model which is
generalizable when it comes to unseen data. Choosing the right cross-validation
depends on the dataset you are dealing with, and one’s choice of cross-validation
on one dataset may or may not apply to other datasets. However, there are a few
types of cross-validation techniques which are the most popular and widely used.

These include:
• k-fold cross-validation
• stratified k-fold cross-validation
• hold-out based validation
• leave-one-out cross-validation
• group k-fold cross-validation

• __k-fold cross-validation__
	We can use this process with almost all kinds of datasets. 
For example, when you have images, you can create a CSV with 
image id, image location and image label and use the process above.
simple k-fold cross-validation works for any regression problem
However, if you see that the distribution of targets is not
consistent, you can use stratified k-fold.

• __stratified k-fold cross-validation__
	If you have a skewed dataset for binary classification with 90% positive 
samples and only 10% negative samples Stratified k-fold cross-validation keeps 
the ratio of labels in each fold constant. So, in each fold, you will have the
same 90% positive and 10% negative samples. Thus, whatever metric you choose to
evaluate, it will give similar results across all folds.
	Some classes have a lot of samples, and some don’t have that many. If we 
do a simple k-fold, we won’t have an equal distribution of targets in every fold. 
Thus, we choose stratified k-fold in this case.
___The rule is simple. If it’s a standard classification problem, choose stratified k-fold
blindly.___
