'''If you have a skewed dataset for binary classification with 90% positive 
samples and only 10% negative samples Stratified k-fold cross-validation keeps 
the ratio of labels in each fold constant. So, in each fold, you will have the
same 90% positive and 10% negative samples. Thus, whatever metric you choose to
evaluate, it will give similar results across all folds.'''

import pandas as pd 
from sklearn import model_selection

TRAIN_PATH = ''




if __name__ == "__main__":
    df = pd.read_csv(TRAIN_PATH)
    # we create a new column called kfold and fill it with -1
    df["kfold"] = -1
    
    # Randomise the rows 
    df = df.sample(frac=1).reset_index(drop=True)
    
    # fetch targets
    y = df.target.values
    
    #initiate the kfold class from model_selection module
    kf = model_selection.StratifiedKFold(n_splits=5)
    
    #fill the new kfold column
    for f, (t_, v_) in enumerate(kf.split(X=df, y=y)):
        df.loc[v_, 'kfold'] = f
        
    # save the new csv with kfold column 
    df.to_csv("train_fold.csv", index = False)
    